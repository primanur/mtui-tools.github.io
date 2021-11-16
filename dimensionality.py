%% library
import numpy as np
#%% dimensionality integration
def frequency(freq):
    freqNew = []
    for i in range(len(freq)):
        for j in range(len(freq[i])):
            freqNew.append(freq[i][j])
    return freqNew

def ellips(freq, Zxxr, Zxxi, Zxyr, Zxyi, Zyxr, Zyxi, Zyyr, Zyyi):
    ## Extract Value
    freqNew = []
    for i in range(len(freq)):
        for j in range(len(freq[i])):
            freqNew.append(freq[i][j])
    
    ZxxrNew = []
    for i in range(len(freq)):
        for j in range(len(Zxxr[i])):
            ZxxrNew.append(Zxxr[i][j])
    
    ZxxiNew = []
    for i in range(len(freq)):
        for j in range(len(Zxxi[i])):
            ZxxiNew.append(Zxxi[i][j])
    
    ZxyrNew = []
    for i in range(len(freq)):
        for j in range(len(Zxyr[i])):
            ZxyrNew.append(Zxyr[i][j])
            
    ZxyiNew = []
    for i in range(len(freq)):
        for j in range(len(Zxyi[i])):
            ZxyiNew.append(Zxyi[i][j])
    
    ZyxrNew = []
    for i in range(len(freq)):
        for j in range(len(Zyxr[i])):
            ZyxrNew.append(Zyxr[i][j])
    
    ZyxiNew = []
    for i in range(len(freq)):
        for j in range(len(Zyxi[i])):
            ZyxiNew.append(Zyxi[i][j])
    
    ZyyrNew = []
    for i in range(len(freq)):
        for j in range(len(Zyyr[i])):
            ZyyrNew.append(Zyyr[i][j])
    
    ZyyiNew = []
    for i in range(len(freq)):
        for j in range(len(Zyyi[i])):
            ZyyiNew.append(Zyyi[i][j])
    ## Matriks impedance
    MatriksZ = [[],[]],[[],[]] 
    for i in range(len(freqNew)):
        MatriksZ[0][0].append((ZyyrNew[i]*ZxxiNew[i])-(ZyxrNew[i]*ZxyiNew[i]))
        MatriksZ[0][1].append((ZyyrNew[i]*ZyxiNew[i])-(ZyxrNew[i]*ZyyiNew[i]))
        MatriksZ[1][0].append((ZxxrNew[i]*ZxyiNew[i])-(ZxyrNew[i]*ZxxiNew[i]))
        MatriksZ[1][1].append((ZxxrNew[i]*ZyyiNew[i])-(ZxyrNew[i]*ZyxiNew[i]))    
    ## Determinan 
    deter = []
    for i in range(len(freqNew)):
        deter.append((ZxxrNew[i]*ZyyrNew[i])-(ZyxrNew[i]*ZxyrNew[i]))
    
    ## Matriks PT
    MatriksPT = [[],[]],[[],[]]
    for i in range(len(freqNew)):
        MatriksPT[0][0].append((MatriksZ[0][0][i]/deter[i]))
        MatriksPT[0][1].append((MatriksZ[0][1][i]/deter[i]))
        MatriksPT[1][0].append((MatriksZ[1][0][i]/deter[i]))
        MatriksPT[1][1].append((MatriksZ[1][1][i]/deter[i]))    
    ## Independant Invariants
    II1, II2 = [], []
    for i in range(len(freqNew)):
        II1.append(0.5*np.sqrt((MatriksPT[0][0][i]-MatriksPT[1][1][i])**2+
                               (MatriksPT[0][1][i]+MatriksPT[1][0][i])**2))
        II2.append(0.5*np.sqrt((MatriksPT[0][0][i]+MatriksPT[1][1][i])**2+
                               (MatriksPT[0][1][i]-MatriksPT[1][0][i])**2))
    ## phase max dan phase min
    phasemax, phasemin = [], []
    for i in range(len(freqNew)):
        phasemax.append((II2[i]+II1[i]))
        phasemin.append((II2[i]-II1[i]))
    ## ellipticity
    ellipticity = []
    for i in range(len(freqNew)):
        ellipticity.append((phasemax[i]-phasemin[i])/(phasemax[i]+phasemin[i]))
    
    return ellipticity

def skewswift(freq, Zxxr, Zxxi, Zxyr, Zxyi, Zyxr, Zyxi, Zyyr, Zyyi):
    ## Extract Value
    freqNew = []
    for i in range(len(freq)):
        for j in range(len(freq[i])):
            freqNew.append(freq[i][j])
    
    ZxxrNew = []
    for i in range(len(freq)):
        for j in range(len(Zxxr[i])):
            ZxxrNew.append(Zxxr[i][j])
    
    ZxxiNew = []
    for i in range(len(freq)):
        for j in range(len(Zxxi[i])):
            ZxxiNew.append(Zxxi[i][j])
    
    ZxyrNew = []
    for i in range(len(freq)):
        for j in range(len(Zxyr[i])):
            ZxyrNew.append(Zxyr[i][j])
            
    ZxyiNew = []
    for i in range(len(freq)):
        for j in range(len(Zxyi[i])):
            ZxyiNew.append(Zxyi[i][j])
    
    ZyxrNew = []
    for i in range(len(freq)):
        for j in range(len(Zyxr[i])):
            ZyxrNew.append(Zyxr[i][j])
    
    ZyxiNew = []
    for i in range(len(freq)):
        for j in range(len(Zyxi[i])):
            ZyxiNew.append(Zyxi[i][j])
    
    ZyyrNew = []
    for i in range(len(freq)):
        for j in range(len(Zyyr[i])):
            ZyyrNew.append(Zyyr[i][j])
    
    ZyyiNew = []
    for i in range(len(freq)):
        for j in range(len(Zyyi[i])):
            ZyyiNew.append(Zyyi[i][j])
            
    # Impedance tensor
    Zxx, Zxy, Zyx, Zyy = [], [], [], []
    for i in range(len(freqNew)):
        Zxx.append(complex(ZxxrNew[i], ZxxiNew[i]))
        Zxy.append(complex(ZxyrNew[i], ZxyiNew[i]))
        Zyx.append(complex(ZyxrNew[i], ZyxiNew[i]))
        Zyy.append(complex(ZyyrNew[i], ZyyiNew[i]))    
    # Calculate Skew
    skew = []
    for i in range(len(freqNew)):
        skew.append(abs((Zxx[i]+Zyy[i])/(Zxy[i]-Zyx[i])))
    
    return skew

def skewbahr(freq, Zxxr, Zxxi, Zxyr, Zxyi, Zyxr, Zyxi, Zyyr, Zyyi):
    ## Extract Value
    freqNew = []
    for i in range(len(freq)):
        for j in range(len(freq[i])):
            freqNew.append(freq[i][j])
    
    ZxxrNew = []
    for i in range(len(freq)):
        for j in range(len(Zxxr[i])):
            ZxxrNew.append(Zxxr[i][j])
    
    ZxxiNew = []
    for i in range(len(freq)):
        for j in range(len(Zxxi[i])):
            ZxxiNew.append(Zxxi[i][j])
    
    ZxyrNew = []
    for i in range(len(freq)):
        for j in range(len(Zxyr[i])):
            ZxyrNew.append(Zxyr[i][j])
            
    ZxyiNew = []
    for i in range(len(freq)):
        for j in range(len(Zxyi[i])):
            ZxyiNew.append(Zxyi[i][j])
    
    ZyxrNew = []
    for i in range(len(freq)):
        for j in range(len(Zyxr[i])):
            ZyxrNew.append(Zyxr[i][j])
    
    ZyxiNew = []
    for i in range(len(freq)):
        for j in range(len(Zyxi[i])):
            ZyxiNew.append(Zyxi[i][j])
    
    ZyyrNew = []
    for i in range(len(freq)):
        for j in range(len(Zyyr[i])):
            ZyyrNew.append(Zyyr[i][j])
    
    ZyyiNew = []
    for i in range(len(freq)):
        for j in range(len(Zyyi[i])):
            ZyyiNew.append(Zyyi[i][j])
            
    # Impedance tensor
    Zxx, Zxy, Zyx, Zyy = [], [], [], []
    for i in range(len(freqNew)):
        Zxx.append(complex(ZxxrNew[i], ZxxiNew[i]))
        Zxy.append(complex(ZxyrNew[i], ZxyiNew[i]))
        Zyx.append(complex(ZyxrNew[i], ZyxiNew[i]))
        Zyy.append(complex(ZyyrNew[i], ZyyiNew[i]))
    # Calculate skew
    Skewbahr = []
    for i in range(len(freqNew)):
        A = ZxxrNew[i]*ZyxiNew[i]
        B = ZyyrNew[i]*ZxyiNew[i]
        C = ZxyrNew[i]*ZyyiNew[i]
        D = ZyxrNew[i]*ZxxiNew[i]
        E = Zxy[i]-Zyx[i]
        Skewbahr.append(np.sqrt(2*(abs(A-B+C-D))/(abs(E))))
    
    return Skewbahr

def strikeanalysis(freq, Zxxr, Zxxi, Zxyr, Zxyi, Zyxr, Zyxi, Zyyr, Zyyi):
    ## Extract Value
    freqNew = []
    for i in range(len(freq)):
        for j in range(len(freq[i])):
            freqNew.append(freq[i][j])
    
    ZxxrNew = []
    for i in range(len(freq)):
        for j in range(len(Zxxr[i])):
            ZxxrNew.append(Zxxr[i][j])
    
    ZxxiNew = []
    for i in range(len(freq)):
        for j in range(len(Zxxi[i])):
            ZxxiNew.append(Zxxi[i][j])
    
    ZxyrNew = []
    for i in range(len(freq)):
        for j in range(len(Zxyr[i])):
            ZxyrNew.append(Zxyr[i][j])
            
    ZxyiNew = []
    for i in range(len(freq)):
        for j in range(len(Zxyi[i])):
            ZxyiNew.append(Zxyi[i][j])
    
    ZyxrNew = []
    for i in range(len(freq)):
        for j in range(len(Zyxr[i])):
            ZyxrNew.append(Zyxr[i][j])
    
    ZyxiNew = []
    for i in range(len(freq)):
        for j in range(len(Zyxi[i])):
            ZyxiNew.append(Zyxi[i][j])
    
    ZyyrNew = []
    for i in range(len(freq)):
        for j in range(len(Zyyr[i])):
            ZyyrNew.append(Zyyr[i][j])
    
    ZyyiNew = []
    for i in range(len(freq)):
        for j in range(len(Zyyi[i])):
            ZyyiNew.append(Zyyi[i][j])
    # Impedance tensor
    Zxx, Zxy, Zyx, Zyy = [], [], [], []
    for i in range(len(freqNew)):
        Zxx.append(complex(ZxxrNew[i], ZxxiNew[i]))
        Zxy.append(complex(ZxyrNew[i], ZxyiNew[i]))
        Zyx.append(complex(ZyxrNew[i], ZyxiNew[i]))
        Zyy.append(complex(ZyyrNew[i], ZyyiNew[i]))
    # Calculate Strike
    Strike = []
    Strike1 = []
    for i in range(len(freqNew)):
        A = (Zxy[i]-Zyx[i])*(Zxx[i]+Zyy[i])
        B = (Zxx[i]-Zyy[i])**2
        C = (Zxy[i]+Zyx[i])**2
        Strike.append(0.25*(np.arctan((2*(A.real))/(B-C))))
        Strike1.append(np.rad2deg(Strike[i].real))
        
    return Strike1
