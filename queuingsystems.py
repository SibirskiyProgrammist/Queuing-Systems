import math

def calculation(_lambda, service_coef, length):
    mu = 1 / service_coef
    print(f"Requests (mu): {mu} = 1 / {service_coef}")
    ro = _lambda / mu
    print(f"Ro: {ro} = {_lambda} / {mu}")
    p0_znam = 1 + ro
    for i in range(2, length):
        p0_znam += math.pow(ro, i) / math.factorial(i)
    p0 = 1 / p0_znam
    print(f"Final probability of event S0: {p0}")
    final_probability = []
    final_probability.append(ro * p0)
    for i in range(2, length):
        final_probability.append((math.pow(ro, i) / math.factorial(i)) * p0)
    probability_refuse = final_probability[-1]
    print(f"Final probabilities of the rest: {final_probability}; \nProbability refuse: {probability_refuse}")
    Q = 1 - probability_refuse
    print(f"Relative throughput: {Q} = 1 - {probability_refuse}")
    A = _lambda * Q
    print(f"Absolute throughput: {A} = {_lambda} * {Q}")

    occupance_channels = A / mu
    print(f"Average number of busy channels: {occupance_channels} = {A} / {mu}")

def main():
    try:
        _lambda = int(input("Enter the lambda value: "))
        service_value = float(input("Enter the service value: "))
        length = int(input("Enter the length: "))

        calculation(_lambda, service_value, length)
    except ValueError:
        print("Incorrect value!")

if __name__ == "__main__":
    main()