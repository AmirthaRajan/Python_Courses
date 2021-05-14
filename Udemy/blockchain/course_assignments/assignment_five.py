import random
import datetime

# Print floatingpoint number between 0 to 1
print(random.uniform(0,1))

# Print random number between 1 to 10
print(random.randrange(1,10,1))

# Print time based on random values
print(datetime.time(random.randrange(0,12,1),random.randrange(0,60,1),random.randrange(0,60,1),random.randrange(0,999999,1)))