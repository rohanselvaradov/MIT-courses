# -*- coding: utf-8 -*-
# Problem Set 5: Experimental Analysis
# Name: 
# Collaborators (discussion):
# Time:

import pylab
import re

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

TRAINING_INTERVAL = range(1961, 2010)
TESTING_INTERVAL = range(2010, 2016)

"""
Begin helper code
"""
class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature
            
        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a 1-d pylab array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return pylab.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]

def se_over_slope(x, y, estimated, model):
    """
    For a linear regression model, calculate the ratio of the standard error of
    this fitted curve's slope to the slope. The larger the absolute value of
    this ratio is, the more likely we have the upward/downward trend in this
    fitted curve by chance.
    
    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by a linear
            regression model
        model: a pylab array storing the coefficients of a linear regression
            model

    Returns:
        a float for the ratio of standard error of slope to slope
    """
    assert len(y) == len(estimated)
    assert len(x) == len(estimated)
    EE = ((estimated - y)**2).sum()
    var_x = ((x - x.mean())**2).sum()
    SE = pylab.sqrt(EE/(len(x)-2)/var_x)
    return SE/model[0]

"""
End helper code
"""

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        degs: a list of degrees of the fitting polynomial

    Returns:
        a list of pylab arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    models = []
    for degree in degs:
        models.append(pylab.polyfit(x, y, degree))
    return models


def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    
    Args:
        y: 1-d pylab array with length N, representing the y-coordinates of the
            N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the R-squared error term
    """
    std_error = ((y - estimated) ** 2).sum()
    variance = ((y - pylab.mean(y)) ** 2).sum()
    return 1 - (std_error / variance)

def evaluate_models_on_training(x, y, models, ylabel="Degrees celsius", xlabel="Years"):
    """
    For each regression model, compute the R-squared value for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points,
        and SE/slope (if degree of this model is 1 -- see se_over_slope). 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    for model in models:
        estimated = pylab.polyval(model, x)
        r2 = r_squared(y, estimated)
        se = ''
        degree = len(model) - 1
        linear = False
        if len(model) == 2:
            se = str(se_over_slope(x, y, estimated, model))
            linear = True
        pylab.plot(x, y, 'bo', label = "Data")
        pylab.plot(x, estimated, 'r-')
        pylab.xlabel(xlabel)
        pylab.ylabel(ylabel)
        title = "Degree = " + str(degree) + "\n" + "R^2 = " + str(r2)
        if linear:
            title += "\n" + "SE = " + se
        pylab.title(title)
        pylab.show()
        

def gen_cities_avg(climate, multi_cities, years):
    """
    Compute the average annual temperature over multiple cities.

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to average over (list of str)
        years: the range of years of the yearly averaged temperature (list of
            int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the average annual temperature over the given
        cities for a given year.
    """
    multi_city_averages = []
    for year in years:
        city_averages = []
        for city in multi_cities:
            daily_data_for_year = climate.get_yearly_temp(city, year)
            city_averages.append(sum(daily_data_for_year) / len(daily_data_for_year))
        multi_city_averages.append(sum(city_averages) / len(city_averages))
    return pylab.array(multi_city_averages)

def moving_average(y, window_length):
    """
    Compute the moving average of y with specified window length.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        window_length: an integer indicating the window length for computing
            moving average

    Returns:
        an 1-d pylab array with the same length as y storing moving average of
        y-coordinates of the N sample points
    """
    averages = pylab.array([])
    i = 1
    while i < window_length:
        averages = pylab.append(averages, (sum(y[0:i]) / i))
        i += 1
    for j in range(i, len(y) + 1):
        averages = pylab.append(averages, (sum(y[j - window_length:j]) / window_length))
    return averages

def rmse(y, estimated):
    """
    Calculate the root mean square error term.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the root mean square error term
    """
    numerator = 0
    for i in range(len(y)):
        numerator += (y[i] - estimated[i]) ** 2
    return (numerator / len(y)) ** 0.5



def gen_std_devs(climate, multi_cities, years):
    """
    For each year in years, compute the standard deviation over the averaged yearly
    temperatures for each city in multi_cities. 

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to use in our std dev calculation (list of str)
        years: the range of years to calculate standard deviation for (list of int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the standard deviation of the average annual 
        city temperatures for the given cities in a given year.
    """
    # TODO
    std_devs = []
    for year in years:
        if year % 4 == 0:
            daily_totals = pylab.zeros(366)
        else:
            daily_totals = pylab.zeros(365)
        for city in multi_cities:
            daily_totals += climate.get_yearly_temp(city, year)
        daily_averages = daily_totals / len(multi_cities)
        yearly_mean = pylab.mean(daily_averages)
        sum_squares = 0
        for day in daily_averages:
            sum_squares += (yearly_mean - day) ** 2
        std_devs.append((sum_squares / len(daily_averages)) ** 0.5)
    return pylab.array(std_devs)

def evaluate_models_on_testing(x, y, models):
    """
    For each regression model, compute the RMSE for this model and plot the
    test data along with the model’s estimation.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        RMSE of your model evaluated on the given data points. 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    for model in models:
        estimated = pylab.polyval(model, x)
        error = rmse(y, estimated)
        degree = len(model) - 1
        pylab.plot(x, y, 'bo', label = "Data")
        pylab.plot(x, estimated, 'r-')
        pylab.xlabel("Years")
        pylab.ylabel("Degrees celsius")
        title = "Degree = " + str(degree) + "\n" + "RMSE = " + str(error)
        pylab.title(title)
        pylab.show()
    # y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # estimate = [1, 4, 9, 16, 25, 36, 49, 64, 81]
    # print(rmse(pylab.array(y), pylab.array(estimate)))


if __name__ == '__main__':
    data = Climate('data.csv')
    x = pylab.array([*TRAINING_INTERVAL])
    yearly_averages = gen_cities_avg(data, CITIES, TRAINING_INTERVAL)
    # Part A.4
    
    # # 4.I
    jan_10th_samples = []
    for year in TRAINING_INTERVAL:
        jan_10th_samples.append(data.get_daily_temp("NEW YORK", 1, 10, year))
    samples = pylab.array(jan_10th_samples)
    models = generate_models(x, samples, [1])
    evaluate_models_on_training(x, samples, models)
    
    # 4.II
    annual_samples = []
    for year in TRAINING_INTERVAL:
        daily_data_for_year = data.get_yearly_temp("NEW YORK", year)
        annual_samples.append(sum(daily_data_for_year) / len(daily_data_for_year))
    samples = pylab.array(annual_samples)
    models = generate_models(x, samples, [1])
    evaluate_models_on_training(x, samples, models)
    
    # Part B
    samples = yearly_averages
    models = generate_models(x, samples, [1])
    evaluate_models_on_training(x, samples, models)
    
    # Part C
    samples = moving_average(yearly_averages, 5)
    models = generate_models(x, samples, [1])
    evaluate_models_on_training(x, samples, models)

    # Part D.2
    
    # 2.I
    samples = moving_average(yearly_averages, 5) 
    models = generate_models(x, samples, [1, 2, 20])
    evaluate_models_on_training(x, samples, models)
    
    # 2.II
    x = pylab.array([*TESTING_INTERVAL])
    yearly_averages = gen_cities_avg(data, CITIES, TESTING_INTERVAL)
    samples = moving_average(yearly_averages, 5) 
    evaluate_models_on_testing(x, samples, models)
    
    # Part E
    x = pylab.array([*TRAINING_INTERVAL])
    std_devs = gen_std_devs(data, CITIES, x)
    samples = moving_average(std_devs, 5) 
    models = generate_models(x, samples, [1])
    evaluate_models_on_training(x, samples, models, "Standard deviations")