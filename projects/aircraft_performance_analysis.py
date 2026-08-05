import pandas as pd
import matplotlib.pyplot as plt

# Sample aircraft performance data
data = {
    "Altitude_m": [0, 1000, 2000, 3000, 4000, 5000],
    "ClimbRate_mps": [18, 16.5, 15, 13.2, 11.5, 9.8]
}

df = pd.DataFrame(data)

print(df)

plt.plot(df["Altitude_m"], df["ClimbRate_mps"], marker="o")
plt.title("Aircraft climb rate vs altitude")
plt.xlabel("Altitude (m)")
plt.ylabel("Climb rate (m/s)")
plt.grid(True)
plt.show()
