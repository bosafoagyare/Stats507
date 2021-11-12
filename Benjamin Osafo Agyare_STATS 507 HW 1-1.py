# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Question 0

# ***
# This is *question 0* for [problem set 1](https://jbhender.github.io/Stats507/F21/ps/ps1.html) of [Stats 507](https://jbhender.github.io/Stats507/F21/ps/ps1.html).
#
# > Question 0 is about Markdown.
#
# The next question is about the **Fibonnaci sequence**, $F_n = F_{n−2} + F_{n−1}$. In part **a** we will define a Python function `fib_rec()`.
#
# Below is a …
#
# ### Level 3 Header
#
# Next, we can make a bulleted list:
#
# * Item 1
#  * detail 1
#  * detail 2
# * Item 2
#
# Finally, we can make an enumerated list:
#
# a. Item 1  
# b. Item 2  
# c. Item 3 
# ***
#

# Modules for the codes
import math
import numpy as np
import scipy.stats as spstat
import statistics as st
import warnings
import time
from timeit import default_timer as timer
from prettytable import PrettyTable


# # Question 1 - Fibonnaci Sequence

# ### (a) Recursion

# +
def fib_rec(n, a = 0, b = 1):
    """
    This function returns the nth Fibonnaci number by recursion
    
    Parameters:
      n: the term of the Fibonacci sequence to return
      a: the first term of the Fibonacci sequence
      b: the second term of the Fibonacci sequence
    
    
    Returns:
      int: the nth term of the Fibonacci sequence.
    """
    
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fib_rec(n - 1, b, a + b)

n_7, n_11, n_13 = 7, 11, 13    
print("F("+str(n_7)+") = "+str(fib_rec(n_7)))
print("F("+str(n_11)+") = "+str(fib_rec(n_11)))
print("F("+str(n_13)+") = "+str(fib_rec(n_13)))

# -

# ### (b) For Loop

# +
def fib_for(n, a = 0, b = 1):
    """"
    This function returns the nth Fibonnaci number using for loop
    
    Parameters:
      n: the term of the Fibonacci sequence to return
      a: the first term of the Fibonacci sequence
      b: the second term of the Fibonacci sequence
    
    
    Returns:
      int: the nth term of the Fibonacci sequence.
    """
    
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(b, n):
            c = a + b
            a = b
            b = c
        return b    

n_7, n_11, n_13 = 7, 11, 13    
print("F("+str(n_7)+") = "+str(fib_for(n_7)))
print("F("+str(n_11)+") = "+str(fib_for(n_11)))
print("F("+str(n_13)+") = "+str(fib_for(n_13)))

# -

# ### (c) While Loop

# +
def fib_whl(n, a = 0, b = 1):
    """"
    This function returns the nth Fibonnaci number using while loop
    
    Parameters:
      n: the term of the Fibonacci sequence to return
      a: the first term of the Fibonacci sequence
      b: the second term of the Fibonacci sequence
    
    
    Returns:
      int: the nth term of the Fibonacci sequence
    """
    
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        i = 0
        while i < n+1:
            if i <= 1:
                c = i
            else:
                c = a + b
                a = b
                b = c
            i += 1    
    return c
    
n_7, n_11, n_13 = 7, 11, 13    
print("F("+str(n_7)+") = "+str(fib_whl(n_7)))
print("F("+str(n_11)+") = "+str(fib_whl(n_11)))
print("F("+str(n_13)+") = "+str(fib_whl(n_13)))   


# -

# ### (d) Rounding

# +
def fib_rnd(n, a = 0, b = 1):
    """"
    This function returns the nth Fibonnaci number using rounding method
    
    Parameters:
      n: the term of the Fibonacci sequence to return
      a: the first term of the Fibonacci sequence
      b: the second term of the Fibonacci sequence
    
    
    Returns:
      int: the nth term of the Fibonacci sequence.
    """
    
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        rho_n = ((1 + math.sqrt(5))/2)**n
        f_n   = rho_n/math.sqrt(5)
    return math.ceil(f_n)
    
n_7, n_11, n_13 = 7, 11, 13    
print("F("+str(n_7)+") = "+str(fib_rnd(n_7)))
print("F("+str(n_11)+") = "+str(fib_rnd(n_11)))
print("F("+str(n_13)+") = "+str(fib_rnd(n_13)))   


# -

# ### (e) Truncation

# +
def fib_flr(n, a = 0, b = 1):
    """"
    This function returns the nth Fibonnaci number using truncation method
    
    Parameters:
      n: the term of the Fibonacci sequence to return
      a: the first term of the Fibonacci sequence
      b: the second term of the Fibonacci sequence
    
    
    Returns:
      int: the nth term of the Fibonacci sequence.
    """
    
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        rho_n = ((1 + math.sqrt(5))/2)**n
        f_n   = (rho_n/math.sqrt(5)) + .5
    return math.floor(f_n)
    
n_7, n_11, n_13 = 7, 11, 13    
print("F("+str(n_7)+") = "+str(fib_flr(n_7)))
print("F("+str(n_11)+") = "+str(fib_flr(n_11)))
print("F("+str(n_13)+") = "+str(fib_flr(n_13))) 


# -

# ### (f) Comparison of Functions

# +
def timereps(reps, func):
    """
    This function computes the median runtime of a function or expression
    
    Parameters:
      reps: the number of function calls
      func: the function or expression to evaluate
    
    
    Returns:
      float: the median runtime of the func argument.
    """
    
    
    
    elapse = []
    for i in range(0, reps):
        start = timer()
        func
        end = timer()
        elapse.append(end - start)
    return elapse


## n = 50
med_rec_50 = st.median(timereps(reps = 1000000, func = fib_rec(50)))
med_for_50 = st.median(timereps(reps = 1000000, func = fib_for(50)))
med_whl_50 = st.median(timereps(reps = 1000000, func = fib_whl(50)))
med_rnd_50 = st.median(timereps(reps = 1000000, func = fib_rnd(50)))
med_flr_50 = st.median(timereps(reps = 1000000, func = fib_flr(50)))


## n = 500
med_rec_500 = st.median(timereps(reps = 1000000, func = fib_rec(500)))
med_for_500 = st.median(timereps(reps = 1000000, func = fib_for(500)))
med_whl_500 = st.median(timereps(reps = 1000000, func = fib_whl(500)))
med_rnd_500 = st.median(timereps(reps = 1000000, func = fib_rnd(500)))
med_flr_500 = st.median(timereps(reps = 1000000, func = fib_flr(500)))

## n = 700
med_rec_700 = st.median(timereps(reps = 1000000, func = fib_rec(700)))
med_for_700 = st.median(timereps(reps = 1000000, func = fib_for(700)))
med_whl_700 = st.median(timereps(reps = 1000000, func = fib_whl(700)))
med_rnd_700 = st.median(timereps(reps = 1000000, func = fib_rnd(700)))
med_flr_700 = st.median(timereps(reps = 1000000, func = fib_flr(700)))

## n = 1000
med_rec_1e4 = st.median(timereps(reps = 1000000, func = fib_rec(1000)))
med_for_1e4 = st.median(timereps(reps = 1000000, func = fib_for(1000)))
med_whl_1e4 = st.median(timereps(reps = 1000000, func = fib_whl(1000)))
med_rnd_1e4 = st.median(timereps(reps = 1000000, func = fib_rnd(1000)))
med_flr_1e4 = st.median(timereps(reps = 1000000, func = fib_flr(1000)))




# +
tab_c = PrettyTable()
tab_c.field_names = ["n", "Function", "Median Runtime"]


### Median Runtime Table ###
# n = 50
tab_c.add_row([50, "recursive", med_rec_50])
tab_c.add_row(["", "for loop", med_for_50])
tab_c.add_row(["", "while loop", med_whl_50])
tab_c.add_row(["", "rounding", med_rnd_50])
tab_c.add_row(["", "truncation", med_flr_50])
tab_c.add_row(["", "", ""])
tab_c.add_row(["", "", ""])


# n = 500
tab_c.add_row([500, "recursive", med_rec_500])
tab_c.add_row(["", "for loop", med_for_500])
tab_c.add_row(["", "while loop", med_whl_500])
tab_c.add_row(["", "rounding", med_rnd_500])
tab_c.add_row(["", "truncation", med_flr_500])
tab_c.add_row(["", "", ""])
tab_c.add_row(["", "", ""])

# n = 700
tab_c.add_row([700, "recursive", med_rec_700])
tab_c.add_row(["", "for loop", med_for_700])
tab_c.add_row(["", "while loop", med_whl_700])
tab_c.add_row(["", "rounding", med_rnd_700])
tab_c.add_row(["", "truncation", med_flr_700])
tab_c.add_row(["", "", ""])
tab_c.add_row(["", "", ""])

# n = 1000
tab_c.add_row([1000, "recursive", med_rec_1e4])
tab_c.add_row(["", "for loop", med_for_1e4])
tab_c.add_row(["", "while loop", med_whl_1e4])
tab_c.add_row(["", "rounding", med_rnd_1e4])
tab_c.add_row(["", "truncation", med_flr_1e4])
tab_c.add_row(["", "", ""])
tab_c.add_row(["", "", ""])

## Output HTML
#print(tab_c.get_html_string())
# -

# <table>
#     <thead>
#         <tr>
#             <th>n</th>
#             <th>Function</th>
#             <th>Median Runtime</th>
#         </tr>
#     </thead>
#     <tbody>
#         <tr>
#             <td>50</td>
#             <td>recursive</td>
#             <td>8.300048648379743e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td>for loop</td>
#             <td>4.2000465327873826e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td>while loop</td>
#             <td>4.2000465327873826e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td>rounding</td>
#             <td>4.2000465327873826e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td>truncation</td>
#             <td>4.2000465327873826e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td></td>
#             <td></td>
#         </tr>
#         <tr>
#             <td></td>
#             <td></td>
#             <td></td>
#         </tr>
#         <tr>
#             <td>500</td>
#             <td>recursive</td>
#             <td>4.2000465327873826e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td>for loop</td>
#             <td>4.2000465327873826e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td>while loop</td>
#             <td>4.2000465327873826e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td>rounding</td>
#             <td>4.2000465327873826e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td>truncation</td>
#             <td>4.2000465327873826e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td></td>
#             <td></td>
#         </tr>
#         <tr>
#             <td></td>
#             <td></td>
#             <td></td>
#         </tr>
#         <tr>
#             <td>700</td>
#             <td>recursive</td>
#             <td>4.2000465327873826e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td>for loop</td>
#             <td>4.2000465327873826e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td>while loop</td>
#             <td>4.2000465327873826e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td>rounding</td>
#             <td>4.2000465327873826e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td>truncation</td>
#             <td>4.2000465327873826e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td></td>
#             <td></td>
#         </tr>
#         <tr>
#             <td></td>
#             <td></td>
#             <td></td>
#         </tr>
#         <tr>
#             <td>1000</td>
#             <td>recursive</td>
#             <td>4.2000465327873826e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td>for loop</td>
#             <td>4.2000465327873826e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td>while loop</td>
#             <td>4.2000465327873826e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td>rounding</td>
#             <td>4.2000465327873826e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td>truncation</td>
#             <td>4.2000465327873826e-08</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td></td>
#             <td></td>
#         </tr>
#         <tr>
#             <td></td>
#             <td></td>
#             <td></td>
#         </tr>
#     </tbody>
# </table>

# It appears that median runtimes are generally uniform across all functions functions at various values of *n*.

# # Question 2

# ### (a) Nth row of pascal triangles

# +
def pascal_nth_row(n):
    """
    This function generates the nth row of Pascal's triangle
    
    Parameters:
      n: the row of the Pascal's triangle to return
    
    
    Returns:
      str: the nth row of Pascal's triangle.
    """

    init = 1
    print(init, end = '')

    for i in range(1, n + 1):

        nxt = (init * (n - i + 1)) // i
        print(" ", nxt, end = '')
        init = nxt


pascal_nth_row(n = 12)


# -

# ### (b) First n rows of Pascal’s triangle

# +
def pascal_triangle(n):
    """
    This function generates the first n rows of Pascal's triangle 
    
    Parameters:
      n: the number of rows of the Pascal's triangle to return
    
    
    Returns:
      the n rows of Pascal's triangle.
    """
    
    for i in range(1, n+1):
        for j in range(0, n-i+1):
            print(' ', end='  ')
 
        val = 1
        for j in range(1, i+1):
            print(' ', val, sep='  ', end=' ')
            val = val * (i - j) // j
        print()
    
pascal_triangle(10)


# -

# # Question 3

# ### (a) Normal Theory

def normal_mean_conf_int(data, conf_level, style = "Default"):
    """"
    This function computes the mean and confidence interval for a 1-dim array 
    
    Parameters:
      data: a 1-dim array of numbers
      conf_level: the confidence level of the test
      style: controls the formatting style of the output. 
             Options include "None" and "Default"
    
    
    Returns:
      a string or a dictiontionary if the style argument is set to 'None'.
    """
    
    data   = np.array(data)
    level  = conf_level/100
    alpha  = 1 - level
    n      = len(data)
    # check if data is 1-dim array
    dim_data = data.ndim
    if dim_data != 1:
        return("Please enter a 1-dimensional array as your input data")
    else:
        est      = np.mean(data)
        se       = np.std(data, ddof=1) / np.sqrt(n)
        z        = spstat.norm.ppf(1 - alpha/2)
        err      = se * z
        lwr, upr = est - err, est + err
        
        # Check for format to return
        if str(style) == "None":
            out = {"est"   : est,
                   "lwr"   : lwr,
                   "upr"   : upr
                  }
            return out
        else:
            out = str(est)+"["+str(conf_level)+"% CI: ("+str(lwr)+", "+str(upr)+")]"
            return out 


# ### (b) Binomial Distribution

def binom_mean_conf_int(data, conf_level, style = "Default", method = "Normal_Approx"):
    """"
    This function computes the mean and confidence interval for a 1-dim array 
    
    Parameters:
      data: a 1-dim array of numbers
      conf_level: the confidence level of the test
      method: controls the method for calculationg the confidence interval
              Options include: Normal_Approx, Clopper_Pearson, Jeffreys and Agresti_Coull 
      style: controls the formatting style of the output 
             Options include "None" and "Default"
    
    
    Returns:
      a string or a dictiontionary if the style argument is set to 'None'.
    """
    
    data   = np.array(data)
    level  = conf_level/100
    alpha  = 1 - level
    n      = len(data)
    # check if data is 1-dim array
    dim_data = data.ndim
    if dim_data != 1:
        return("Please enter a 1-dimensional array as your input data")
    else:
        x   = np.sum(data)
        est = x/n
        if str(method) == "Normal_Approx":
            se       = (est * (1 - est) / n) ** 0.5
            z        = round(spstat.norm.ppf(1 - alpha/2), 2)
            err      = se * z
            lwr, upr = est - err, est + err
            
            if(min(n*est, n*(1-est)) <= 12):
                 warnings.warn("Approximation is not adequate because min (np, n(1-p)) is not more than 12")
            
        elif str(method) == "Clopper_Pearson":
            lwr   = spstat.beta.ppf(alpha/2, x, (n-x+1))
            upr   = spstat.beta.ppf(1-(alpha/2), (x+1), (n-x)) 
            
        elif str(method) == "Jeffreys":
            alpha = 1 - level
            lwr   = max(0, spstat.beta.ppf(alpha/2, x + 0.5, (n-x+0.5)))
            upr   = min(spstat.beta.ppf(1-(alpha/2), (x + 0.5), (n-x+0.5)), 1)
        
        elif str(method) == "Agresti_Coull":
            z        = spstat.norm.ppf(1 - alpha/2)
            n_new    = n + z**2
            est_new  = (1/n_new)*(x + (z**2)/2)
            se       = (est_new * (1 - est_new) / n_new) ** 0.5
            err      = se * z
            est      = est_new
            lwr, upr = est_new - err, est_new + err
        
        else:
            return("Please choose a method")
        
        
        
        # Check for format to return
        if str(style) == "None":
            out = {"est"   : est,
                   "lwr"   : lwr,
                   "upr"   : upr
                  }
            return out
        else:
            out = str(est)+"["+str(conf_level)+"% CI: ("+str(lwr)+", "+str(upr)+")]"
            return out

# ### (d) Table for comparison of Methods
#

# +
dat = np.array([1]*42 + [0]*48)


### for 90% confidence level
cf_norm_90     = normal_mean_conf_int(data = dat, conf_level = 90,
                                      style = "None") 
cf_binom_NA_90 = binom_mean_conf_int(data = dat, conf_level = 90,
                                     style = "None",
                                     method = "Normal_Approx")
cf_binom_CP_90 = binom_mean_conf_int(data = dat, conf_level = 90,
                    style = "None",
                    method = "Clopper_Pearson")
cf_binom_JF_90 = binom_mean_conf_int(data = dat, conf_level = 90,
                    style = "None",
                    method = "Jeffreys")
cf_binom_AC_90 = binom_mean_conf_int(data = dat, conf_level = 90,
                    style = "None",
                    method = "Agresti_Coull")


### for 95% confidence level
cf_norm_95     = normal_mean_conf_int(data = dat, conf_level = 95,
                                      style = "None") 
cf_binom_NA_95 = binom_mean_conf_int(data = dat, conf_level = 95,
                                     style = "None",
                                     method = "Normal_Approx")
cf_binom_CP_95 = binom_mean_conf_int(data = dat, conf_level = 95,
                    style = "None",
                    method = "Clopper_Pearson")
cf_binom_JF_95 = binom_mean_conf_int(data = dat, conf_level = 95,
                    style = "None",
                    method = "Jeffreys")
cf_binom_AC_95 = binom_mean_conf_int(data = dat, conf_level = 95,
                    style = "None",
                    method = "Agresti_Coull")

### for 99% confidence level
cf_norm_99     = normal_mean_conf_int(data = dat, conf_level = 99,
                                      style = "None") 
cf_binom_NA_99 = binom_mean_conf_int(data = dat, conf_level = 99,
                                     style = "None",
                                     method = "Normal_Approx")
cf_binom_CP_99 = binom_mean_conf_int(data = dat, conf_level = 99,
                    style = "None",
                    method = "Clopper_Pearson")
cf_binom_JF_99 = binom_mean_conf_int(data = dat, conf_level = 99,
                    style = "None",
                    method = "Jeffreys")
cf_binom_AC_99 = binom_mean_conf_int(data = dat, conf_level = 99,
                    style = "None",
                    method = "Agresti_Coull")

# +
tab = PrettyTable()
tab.field_names = ["Method", "Confidence Level (%)", "Lower", "Upper", "Width"]

## 90% CI rows
tab.add_row(["Normal Theory", 90, round(cf_norm_90["lwr"], 4),
             round(cf_norm_90["upr"], 4),
            round(cf_norm_90["upr"], 4) - round(cf_norm_90["lwr"], 4)])
tab.add_row(["Normal Approximation", "", round(cf_binom_NA_90["lwr"], 4),
             round(cf_binom_NA_90["upr"], 4),
            round(cf_binom_NA_90["upr"] - cf_binom_NA_90["lwr"], 4)])
tab.add_row(["Clopper-Pearson Interval", "", round(cf_binom_CP_90["lwr"], 4),
             round(cf_binom_CP_90["upr"], 4),
            round(cf_binom_CP_90["upr"] - cf_binom_CP_90["lwr"], 4)])
tab.add_row(["Jeffreys Interval", "", round(cf_binom_JF_90["lwr"], 4),
             round(cf_binom_JF_90["upr"], 4),
            round(cf_binom_JF_90["upr"] - cf_binom_JF_90["lwr"], 4)])
tab.add_row(["Agresti-Coull Interval", "", round(cf_binom_AC_90["lwr"], 4),
             round(cf_binom_AC_90["upr"], 4),
            round(cf_binom_AC_90["upr"] - cf_binom_AC_90["lwr"], 4)])
tab.add_row(["", "", "", "", ""])
tab.add_row(["", "", "", "", ""])


## 95% CI rows
tab.add_row(["Normal Theory", 95, round(cf_norm_95["lwr"], 4),
             round(cf_norm_95["upr"], 4),
            round(cf_norm_95["upr"] - cf_norm_95["lwr"], 4)])
tab.add_row(["Normal Approximation", "", round(cf_binom_NA_95["lwr"], 4),
             round(cf_binom_NA_95["upr"], 4),
            round(cf_binom_NA_95["upr"] - cf_binom_NA_95["lwr"], 4)])
tab.add_row(["Clopper-Pearson Interval", "", round(cf_binom_CP_95["lwr"], 4),
             round(cf_binom_CP_95["upr"], 4),
            round(cf_binom_CP_95["upr"] - cf_binom_CP_95["lwr"], 4)])
tab.add_row(["Jeffreys Interval", "", round(cf_binom_JF_95["lwr"], 4),
             round(cf_binom_JF_95["upr"], 4),
            round(cf_binom_JF_95["upr"] - cf_binom_JF_95["lwr"], 4)])
tab.add_row(["Agresti-Coull Interval", "", round(cf_binom_AC_95["lwr"], 4),
             round(cf_binom_AC_95["upr"], 4),
            round(cf_binom_AC_95["upr"] - cf_binom_AC_95["lwr"], 4)])
tab.add_row(["", "", "", "", ""])
tab.add_row(["", "", "", "", ""])


## 99% CI rows
tab.add_row(["Normal Theory", 99, round(cf_norm_99["lwr"], 4),
             round(cf_norm_99["upr"], 4),
            round(cf_norm_99["upr"], 4) - round(cf_norm_99["lwr"], 4)])
tab.add_row(["Normal Approximation", "", round(cf_binom_NA_99["lwr"], 4),
             round(cf_binom_NA_99["upr"], 4),
            round(cf_binom_NA_99["upr"] - cf_binom_NA_99["lwr"], 4)])
tab.add_row(["Clopper-Pearson Interval", "", round(cf_binom_CP_99["lwr"], 4),
             round(cf_binom_CP_99["upr"], 4),
            round(cf_binom_CP_99["upr"] - cf_binom_CP_99["lwr"], 4)])
tab.add_row(["Jeffreys Interval", "", round(cf_binom_JF_99["lwr"], 4),
             round(cf_binom_JF_99["upr"], 4),
            round(cf_binom_JF_99["upr"] - cf_binom_JF_99["lwr"], 4)])
tab.add_row(["Agresti-Coull Interval", "", round(cf_binom_AC_99["lwr"], 4),
             round(cf_binom_AC_99["upr"], 4),
            round(cf_binom_AC_99["upr"] - cf_binom_AC_99["lwr"], 4)])
tab.add_row(["", "", "", "", ""])
tab.add_row(["", "", "", "", ""])

## Generate ASCII and HTML Table (uncommSent to run)
#print(tab)
#print(tab.get_html_string())
# -

# <table>
#     <thead>
#         <tr>
#             <th>Method</th>
#             <th>Confidence Level (%)</th>
#             <th>Lower</th>
#             <th>Upper</th>
#             <th>Width</th>
#         </tr>
#     </thead>
#     <tbody>
#         <tr>
#             <td>Normal Theory</td>
#             <td>90</td>
#             <td>0.3797</td>
#             <td>0.5536</td>
#             <td>0.1739</td>
#         </tr>
#         <tr>
#             <td>Normal Approximation</td>
#             <td></td>
#             <td>0.3804</td>
#             <td>0.5529</td>
#             <td>0.1725</td>
#         </tr>
#         <tr>
#             <td>Clopper-Pearson Interval</td>
#             <td></td>
#             <td>0.3765</td>
#             <td>0.5586</td>
#             <td>0.1821</td>
#         </tr>
#         <tr>
#             <td>Jeffreys Interval</td>
#             <td></td>
#             <td>0.3818</td>
#             <td>0.5531</td>
#             <td>0.1712</td>
#         </tr>
#         <tr>
#             <td>Agresti-Coull Interval</td>
#             <td></td>
#             <td>0.3824</td>
#             <td>0.5529</td>
#             <td>0.1705</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td></td>
#             <td></td>
#             <td></td>
#             <td></td>
#         </tr>
#         <tr>
#             <td></td>
#             <td></td>
#             <td></td>
#             <td></td>
#             <td></td>
#         </tr>
#         <tr>
#             <td>Normal Theory</td>
#             <td>95</td>
#             <td>0.363</td>
#             <td>0.5703</td>
#             <td>0.2073</td>
#         </tr>
#         <tr>
#             <td>Normal Approximation</td>
#             <td></td>
#             <td>0.3636</td>
#             <td>0.5697</td>
#             <td>0.2061</td>
#         </tr>
#         <tr>
#             <td>Clopper-Pearson Interval</td>
#             <td></td>
#             <td>0.3607</td>
#             <td>0.5749</td>
#             <td>0.2142</td>
#         </tr>
#         <tr>
#             <td>Jeffreys Interval</td>
#             <td></td>
#             <td>0.366</td>
#             <td>0.5694</td>
#             <td>0.2034</td>
#         </tr>
#         <tr>
#             <td>Agresti-Coull Interval</td>
#             <td></td>
#             <td>0.3671</td>
#             <td>0.569</td>
#             <td>0.2019</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td></td>
#             <td></td>
#             <td></td>
#             <td></td>
#         </tr>
#         <tr>
#             <td></td>
#             <td></td>
#             <td></td>
#             <td></td>
#             <td></td>
#         </tr>
#         <tr>
#             <td>Normal Theory</td>
#             <td>99</td>
#             <td>0.3305</td>
#             <td>0.6029</td>
#             <td>0.2724</td>
#         </tr>
#         <tr>
#             <td>Normal Approximation</td>
#             <td></td>
#             <td>0.331</td>
#             <td>0.6023</td>
#             <td>0.2714</td>
#         </tr>
#         <tr>
#             <td>Clopper-Pearson Interval</td>
#             <td></td>
#             <td>0.3306</td>
#             <td>0.6064</td>
#             <td>0.2758</td>
#         </tr>
#         <tr>
#             <td>Jeffreys Interval</td>
#             <td></td>
#             <td>0.3357</td>
#             <td>0.601</td>
#             <td>0.2653</td>
#         </tr>
#         <tr>
#             <td>Agresti-Coull Interval</td>
#             <td></td>
#             <td>0.3382</td>
#             <td>0.5997</td>
#             <td>0.2615</td>
#         </tr>
#         <tr>
#             <td></td>
#             <td></td>
#             <td></td>
#             <td></td>
#             <td></td>
#         </tr>
#         <tr>
#             <td></td>
#             <td></td>
#             <td></td>
#             <td></td>
#             <td></td>
#         </tr>
#     </tbody>
# </table>

# It can be seen from the table that, **Agresti-Coull Interval**, produces the smallest width across all the **90%**, **95%** and **99%** confidence levels with respect to the data
