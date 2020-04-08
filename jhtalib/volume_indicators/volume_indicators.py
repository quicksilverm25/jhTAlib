# Import Built-Ins:

# Import Third-Party:

# Import Homebrew:
import jhtalib as jhta


def AD(df, high='High', low='Low', close='Close', volume='Volume'):
    """
    Chaikin A/D Line
    """
    ad_list = []
    for i in range(len(df[close])):
        ad = 0
        if i > 0:
            clv = ((df[close][i] - df[low][i]) - (df[high][i] - df[close][i])) / (df[high][i] - df[low][i])
            ad = ad_list[i - 1] + clv * df[volume][i]
        ad_list.append(ad)
    return ad_list

def ADOSC(df):
    """
    Chaikin A/D Oscillator
    """

def MFAI(df, high='High', low='Low', volume='Volume'):
    """
    Market Facilitation Index
    """
    return [(df[high][i] - df[low][i]) / df[volume][i] for i in range(len(df[low]))]

def NVI(df, price='Close', volume='Volume'):
    """
    Negative Volume Index
    """
    nvi_list = []
    for i in range(len(df[price])):
        nvi = 0
        if i > 0:
            if df[volume][i] < df[volume][i - 1]:
                nvi = nvi_list[i - 1] + (df[price][i] - df[price][i - 1]) / df[price][i - 1]
            else:
                nvi = nvi_list[i - 1]
        nvi_list.append(nvi)
    return nvi_list

def OBV(df, close='Close', volume='Volume'):
    """
    On Balance Volume
    """
    obv_list = []
    for i in range(len(df[close])):
        obv = 0
        if i > 0:
            if df[close][i] > df[close][i - 1]:
                obv = obv_list[i - 1] + df[volume][i]
            elif df[close][i] < df[close][i - 1]:
                obv = obv_list[i - 1] - df[volume][i]
            else:
                obv = obv_list[i - 1]
        obv_list.append(obv)
    return obv_list

def PVR(df, price='Close', volume='Volume'):
    """
    Price Volume Rank
    """
    pvr_list = []
    for i in range(len(df[price])):
        if i < 1:
            pvr = float('NaN')
        else:
            if df[price][i] > df[price][i - 1] and df[volume][i] > df[volume][i - 1]:
                pvr = 1
            if df[price][i] > df[price][i - 1] and df[volume][i] < df[volume][i - 1]:
                pvr = 2
            if df[price][i] < df[price][i - 1] and df[volume][i] < df[volume][i - 1]:
                pvr = 3
            if df[price][i] < df[price][i - 1] and df[volume][i] > df[volume][i - 1]:
                pvr = 4
        pvr_list.append(pvr)
    return pvr_list

def PVT(df, price='Close', volume='Volume'):
    """
    Price Volume Trend
    """
    pvt_list = []
    for i in range(len(df[price])):
        pvt = 0
        if i > 0:
            pvt = pvt_list[i - 1] + df[volume][i] * (df[price][i] - df[price][i - 1]) / df[price][i - 1]
        pvt_list.append(pvt)
    return pvt_list

def PVI(df, price='Close', volume='Volume'):
    """
    Positive Volume Index
    """
    pvi_list = []
    for i in range(len(df[price])):
        pvi = 0
        if i > 0:
            if df[volume][i] > df[volume][i - 1]:
                pvi = pvi_list[i - 1] + (df[price][i] - df[price][i - 1]) / df[price][i - 1]
            else:
                pvi = pvi_list[i - 1]
        pvi_list.append(pvi)
    return pvi_list

def VWAP(df, open='Open', high='High', low='Low', close='Close', volume='Volume'):
    """
    Volume Weighted Average Price
    """
    vwap_list = []
    pvs = .0
    for i in range(len(df[close])):
        o = df[open][i]
        h = df[high][i]
        l = df[low][i]
        c = df[close][i]
        v = df[volume][i]
#        vwap = sum([o * v/4, h * v/4, l * v/4, c * v/4]) / v
        pvs += (sum([o, h, l, c]) / 4) * v
        vwap = pvs / sum(df[volume][0:i + 1])
        vwap_list.append(vwap)
    return vwap_list

