import pytest
_ = 123456789  # just  wrong number, please ignore

# Black box model
# 1. Calculate the specific yield coefficients (C-mol) for all products.

c-mol glyc = 30.7 g
c-mol etha = 23
biomass = 24.6
c-mol gluc = 30

Y_se + Y_sg + Y_sx = 1



# Add your calculations here ...



# Assign your solutions to the following variables (replace _ with your solutions)
Y_sx = 0.20
Y_se = 0.65
Y_sg = 0.07

def test_Y_sx():
    assert Y_sx == pytest.approx(0.166, .01)

def test_Y_se():
    assert Y_se == pytest.approx(0.652, .01)

def test_Y_sg():
    assert Y_sg == pytest.approx(0.075, .01)
  

# 2. Calculate the carbon balance.

NH3 + CH2O + O2 = CH301/2+ CH8/3 O2/3 + CH1.8O0.5N0.2 

# Add your calculations here ...




# Assign your solution to the following variable (replace _ with your solution)
carbon_balance = 0.93 # c-mol-? / c-mol-Glc

def test_carbon_balance():
    assert carbon_balance == pytest.approx(0.106, 0.01)
    

# 3. Assuming that CO2 is the only missing product, calculate how much CO2 was produced in the fermentation.

# Add your calculations here ...

1 - 0.93 = 0.07 C-mol

# Assign your solution to the following variable (replace _ with your solution)
co2_produced = 1.61 # g/L

def test_co2_produced():
    assert co2_produced == pytest.approx(3.129, 0.01)
    
