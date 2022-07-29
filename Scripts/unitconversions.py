def convert_WperFt2_to_WperM2(WperFt2):
    WperM2 = 10.76*WperFt2
    return WperM2

def convert_degF_to_degC(degF):
    degC = (degF-32)*5/9
    return degC

def convert_degC_to_degF(degC):
    degF = (degC*9/5)+32
    return degF

def convert_IP_Uvalue_to_SI_Uvalue(BtuPerHft2F):
    WperM2K = BtuPerHft2F*5.67446589738871
    return WperM2K

def convert_J_to_kWh(J):
    kWh = J*0.000000277778
    return kWh

def convert_J_to_therm(J):
    therm = J*0.00000000948043
    return therm

def convert_W_to_Btuh(W):
    Btuh = W*3.41
    return Btuh