from numpy import log, sqrt, exp
from scipy.stats import norm


class BlackScholes:
    def __init__(
        self,
        time_to_maturity: float,
        strike: float,
        current_price: float,
        volatility: float,
        interest_rate: float,
    ):
        self.time_to_maturity = time_to_maturity
        self.strike = strike
        self.current_price = current_price
        self.volatility = volatility
        self.interest_rate = interest_rate

    def calculate_prices(self):
        T = self.time_to_maturity
        K = self.strike
        S = self.current_price
        sigma = self.volatility
        r = self.interest_rate

        d1 = (log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * sqrt(T))
        d2 = d1 - sigma * sqrt(T)

        call_price = S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
        put_price = K * exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

        self.call_price = call_price
        self.put_price = put_price

        # Greeks
        self.call_delta = norm.cdf(d1)
        self.put_delta = norm.cdf(d1) - 1

        self.call_gamma = norm.pdf(d1) / (S * sigma * sqrt(T))
        self.put_gamma = self.call_gamma

        self.vega = S * norm.pdf(d1) * sqrt(T)

        self.call_theta = (
            - (S * norm.pdf(d1) * sigma) / (2 * sqrt(T))
            - r * K * exp(-r * T) * norm.cdf(d2)
        )

        self.put_theta = (
            - (S * norm.pdf(d1) * sigma) / (2 * sqrt(T))
            + r * K * exp(-r * T) * norm.cdf(-d2)
        )

        return call_price, put_price
