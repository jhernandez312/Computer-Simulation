import itertools
import random
import numpy as np
import simpy
import read_csv
from read_csv import stations_with_bikes

RANDOM_SEED = 420

MEAN_INTERARRIVAL_TIME = 1/2.38       # mean interarrival time for exponential distribution
SIM_TIME = 1440                       # simulation time in minutes
TOTAL_RIDERS = 3500                   # total number of riders expected
MU = 2.78                           # mean of the log-normal distribution for bike usage time
SIGMA = 0.619                       # standard deviation of the log-normal distribution

start_prob_list = read_csv.start_station('start_station_probs.csv')
return_prob_dict = read_csv.station_data('trip_stats_copy.csv')
STATION_NAMES, STATION_PROBABILITIES = zip(*start_prob_list)  # Unpacking names and probabilities
NUM_STATIONS = len(STATION_NAMES)  # Adjust number of stations based on CSV


class BikeService:
    """A Bike Service with numbered bikes at each station. Each bike can be individually tracked."""

    def __init__(self, env, station_names, bike_counts):
        self.env = env
        self.stations = {name: simpy.Store(env) for name in station_names}
        self.bike_counts = bike_counts.copy()  # Initializes with the starting bike counts
        for station_name in station_names:
            num_bikes = stations_with_bikes.get(station_name, 10)  # default to 10 bikes if not specified in the dictionary
            for i in range(num_bikes):
                self.stations[station_name].put(f'Bike {i+1}')
            #print(f'Station: {station_name}, Number of Bikes: {num_bikes}')

        self.global_wait_count = 0

    def service(self, rider, bike_id, station_name):
        """The service process for a bike at a station."""

        use_time = np.random.lognormal(MU, SIGMA)
        #print(f'{rider} is now using {bike_id} at {station_name} for {use_time:.2f} minutes.')
        yield env.timeout(use_time)

    def add_bike(self, station_name):
        """Method to add a bike dynamically to a station."""
        new_bike_id = f'Bike {len(self.stations[station_name].items) + 1}'
        self.stations[station_name].put(new_bike_id)
        self.bike_counts[station_name] += 1  # update the dictionary with the new count
        print(f'Added {new_bike_id} to {station_name}. Total bikes now: {self.bike_counts[station_name]}')
        print(f'{self.bike_counts}')


def rider(env, name, bs, start_prob_list):
    """Rider process: each rider chooses a station based on predefined probabilities and a bike, and returns it to a random station."""

    station_names = list(bs.stations.keys())
    station_id = np.random.choice(station_names, p=start_prob_list)
    station = bs.stations[station_id]

    #print(f'{name} arrives and approaches station {station_id} at time {env.now:.2f}.')


    if station.items == []:
        print(f'{name} is waiting for a bike at station {station_id}.')
        print(f'{station_id}')
        bs.global_wait_count += 1
        bs.add_bike(station_id)  # dynamically add a bike to the station

        #print({bs.global_wait_count})
    bike_id = yield station.get()  # rider takes a bike from the station
    #print(f'{name} picked {bike_id} at station {station_id} at time {env.now:.2f}.')
    yield env.process(bs.service(name, bike_id, station_id))


    if station_id in station_names:
    # unpack the list of tuples into two lists: one for end stations and one for probabilities
        end_stations, probabilities = zip(*return_prob_dict[station_id])

    probabilities = np.array(probabilities)
    if probabilities.sum() == 0:
        probabilities = np.ones_like(probabilities) / len(probabilities)
    else:
        probabilities /= probabilities.sum()

    return_station_id = np.random.choice(end_stations, p=probabilities)
    return_station = bs.stations[station_id]
    yield return_station.put(bike_id)
    #print(f'{name} returns {bike_id} to end station {return_station_id} and leaves at time {env.now:.2f}.')



def setup(env, station_names, start_prob_list, mean_interarrival, total_riders):
    bike_service = BikeService(env, station_names, stations_with_bikes)
    rider_count = itertools.count()
    riders_created = 0

    while True:
        if riders_created >= total_riders:
            yield env.timeout(1)  # just wait and do nothing, but allow other processes to continue
            continue
        yield env.timeout(np.random.exponential(scale=mean_interarrival))
        env.process(rider(env, f'Rider {next(rider_count)}', bike_service, start_prob_list))
        riders_created += 1

# setup and start the simulation
print('Bike Service Simulation Starting...')
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

env = simpy.Environment()
env.process(setup(env, STATION_NAMES, STATION_PROBABILITIES, MEAN_INTERARRIVAL_TIME, TOTAL_RIDERS))
env.run(until=SIM_TIME)

