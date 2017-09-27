__author__ = 'glennschultz'
import math


def time_value(interest_rate, number_periods, frequency, compound_type):
    """ this function returns time value factor either periodic or continuous compounding
    :param interest_rate double
    :param number_periods double
    :param frequency double
    :param compound_type string
    """
    disc_rate = None
    factor = None

    if compound_type not in list('continuous', 'period'):
        print('invalid compound type')
    else:
        if compound_type == 'period' and disc_rate is None:
            disc_rate = interest_rate / frequency
            if compound_type == 'period' and factor is None:
                factor = (1 + disc_rate) ** -number_periods
            else:
                if compound_type == 'continuous' and disc_rate is None:
                    disc_rate = interest_rate / frequency
                    if compound_type == 'continuous' and factor is None:
                        factor = math.exp(disc_rate * -number_periods)
