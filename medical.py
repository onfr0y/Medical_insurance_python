age = 20
sex = 1
num_of_children = 29
smoker = 1
 
#analyzing the Smoker status
def analyze_smoker(smoker):
    if smoker == 1:
        print("To lower your cost, you should consider quitting smoking.")
    else:
        print("Smoking is not an issue for you.")

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
  estimated_cost = 400*age - 128*sex + 425*num_of_children + 10000*smoker - 2500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  return estimated_cost

def advice_for_smoker(smoker):
  if smoker ==  1 :
    print('you should quit now idiot, its not good for you and your family')
  else :
    print('nice dude , you are a true Man')




 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, num_of_children = 3, smoker = 1)
advice_for_smoker(smoker)
