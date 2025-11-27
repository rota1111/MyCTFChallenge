from fractions import Fraction
import math

# 多项式的辗转相除法
def duc(p, poly_nrt):
       
    rv = [1, -p[0]]
    if len(poly_nrt) == 4:
        result = [1]
        result.append(poly_nrt[1] - rv[1])
        result.append(poly_nrt[2] - result[1] * rv[1])
        result.append(poly_nrt[3] - result[2] * rv[1])
    elif len(poly_nrt) == 3:
        result = [1]
        result.append(poly_nrt[1] - rv[1])
        result.append(poly_nrt[2] - result[1] * rv[1])
    else:
        print('Error! Length of coefficients does not match.')
        return(0)
    
    
    if result[-1] != 0:
        print('Error! Result is Wrong.')
        return(0)
    
    return result[:-1]


#定义加法
def add(p1, p2):
    
    #如果p1、p2是同一个点，那么该处斜率是该点的导数。如果不是同一个点，那么通过坐标可以计算出斜率
    if p1 == p2:
        slope = Fraction(1,2) / p1[1] * (3*p1[0]**2 + 218*p1[0] + 224)    
    else:
        slope = Fraction((p2[1] - p1[1]) / (p2[0] - p1[0]))    
    
    #Function: y - p1[1] = slope * (x - p1[0])
    #直线方程的系数（y = kx + b），k、b即为系数
    coe_line = [slope, p1[1] - slope * p1[0]]
    
    #直线方程代入椭圆方程，计算方程系数
    coe_ellipse = [1, 109 - coe_line[0] **2, 224 - 2 * coe_line[0] * coe_line[1], -coe_line[1]**2]
   
    res_1 = duc(p1, coe_ellipse)
    res_2 = duc(p2, res_1)
    
    x = -res_2[1]
    y = (slope * (x +100) +260) * (-1)
    
    return ([x,y])


p1 = [-100, 260]
p2 = [-100, 260]

a=0
b=0
c=0

#循环数
k=2
#寻找到a、b、c全部大于零为止
while not (a>0 and b>0 and c>0):

    p2 = add(p1,p2)
    
    x = p2[0]
    y = p2[1]
    
    a = Fraction(56-x+y, 56-14*x)
    b = Fraction(56-x-y, 56-14*x)
    c = Fraction(-28-6*x, 28-7*x)
    
    a/(b+c) + b/(a+c) + c/(a+b)
    
    
    #公分母
    common_deno = a.denominator * b.denominator * c.denominator
    
    a = a * common_deno
    b = b * common_deno
    c = c * common_deno
    
    #分子最大公约数
    gcd_numerator = math.gcd(math.gcd(a.numerator, b.numerator), math.gcd(a.numerator, c.numerator))
    
    a = a / gcd_numerator
    b = b / gcd_numerator
    c = c / gcd_numerator
    
    print('循环数 k = ',k)
    print('a = ',a)
    print('b = ',b)
    print('c = ',c)
    
    print('验算结果：',a/(b+c) + b/(a+c) + c/(a+b))
    k+=1