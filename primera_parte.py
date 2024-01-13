from datasets import load_dataset
import numpy as np


dataset = load_dataset("mstz/heart_failure")


data = dataset["train"]


ages = data['age']


ages_array = np.array(ages)


average_age = np.mean(ages_array)

print(f"El promedio de edad es: {average_age}")
