
import math
import re

def ConvertELogStrToValue(eLogStr):

    (convertOK, convertedValue) = (False, 0.0);
    foundEPower = re.search("(?P<coefficientPart>-?\d+\.\d+)e(?P<ePowerPart>-\d+)", eLogStr, re.I);
    # print "foundEPower=",foundEPower;
    if (foundEPower):
        coefficientPart = foundEPower.group("coefficientPart");
        ePowerPart = foundEPower.group("ePowerPart");
        # print "coefficientPart=%s,ePower=%s"%(coefficientPart, ePower);
        coefficientValue = float(coefficientPart);
        ePowerValue = float(ePowerPart);
        # print "coefficientValue=%f,ePowerValue=%f"%(coefficientValue, ePowerValue);
        # math.e= 2.71828182846
        wholeOrigValue = coefficientValue * math.pow(math.e, ePowerValue);
        # print "wholeOrigValue=",wholeOrigValue;

        (convertOK, convertedValue) = (True, wholeOrigValue);
    else:
        (convertOK, convertedValue) = (False, 0.0);

    return (convertOK, convertedValue);