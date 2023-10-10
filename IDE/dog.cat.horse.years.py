"""
Julissa Paramo
8/31/23
Lab 2
"""
#varibales, conversions

print('Enter your age:', end=" ") #statement before input
human_years = float(input()) 

dog_years = human_years * 7 #convert human years to dog years
dog_years1 = dog_years//1 #int division to round down

#convert years to months
dog_months = dog_years * 12 - dog_years1 * 12 #diff between float and int values
final_dog_month = dog_months//1 #int division to round down

dog_days = dog_months % 1 #isolate the float from month value
final_dog_days = (dog_days * 30)//1 #convert months to days, int division to round down

#print final statement for dog age
print('Your age in dog years is ' + str(dog_years1) + ' years ' + str(final_dog_month) + ' months and ' + str(final_dog_days) + ' days')



cat_years = human_years / 9 #convert human years to cat years
cat_years1 = cat_years//1 #int division to round down

#convert years to months
cat_months = (cat_years - cat_years1) * 12 #diff between float and int values
final_cat_month = cat_months//1 #int division to round down

cat_days =cat_months % 1 #isolate float from month value
final_cat_days = cat_days * 30//1 #convert months to days, int division to round down

#print final statement for cat age
print('Your age in cat years is ' + str(cat_years1) + ' years ' + str(final_cat_month) + ' months and ' + str(final_cat_days) + ' days')



horse_years = 3 * ( ( ( human_years**2 ) - 47 ) / 7+12 ) #convert human years to horse years
horse_years1 = horse_years//1 #int division to round down

#convert months to years
horse_months = horse_years * 12 - horse_years1 * 12 #diff between float and int values
final_horse_month = horse_months // 1 #int division to round down

horse_days = horse_months % 1 #isolate float from month value
final_horse_days = horse_days * 30//1 #convert months to days, int division to round down

#print final statement
print('Your age in horse years is ' + str( horse_years1 ) + ' years ' + str( final_horse_month ) + ' months and ' + str( final_horse_days ) + ' days')







