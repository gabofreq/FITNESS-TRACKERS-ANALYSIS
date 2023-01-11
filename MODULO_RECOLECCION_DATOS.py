#!pip install dfply
from dfply import *
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_soup(url):
    r = requests.get('http://localhost:8050/render.html', params = {'url':url,'wait':5})
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_reviews(soup,amazon):
    reviews = soup.find_all('div',{'data-hook':'review'})
    try:
        for item in reviews:
            review = {
                'DEVICE_MODEL':     soup.title.text.replace(amazon,''),
                'TITLE':            item.find('a',{'data-hook':'review-title'}).text.strip(),
                'RATE':             float(item.find('i',{'data-hook':'review-star-rating'}).text.replace('out of 5 stars','').strip()),
                'STATE':            item.find('span',{'data-hook':'avp-badge'}).text.strip(),
                'USER':             item.find('span',{'class':'a-profile-name'}).text.strip(),
                'COUNTRY_DATE':     item.find('span',{'data-hook':'review-date'}).text.replace('Reviewed in the ','').replace('Reviewed in ','').strip(),
                'COMMENTS':         item.find('span',{'data-hook':'review-body'}).text.strip(),
                }
            reviewlist.append(review)
    except:
        pass


##################################################################################################################
################################################## AMAZBIT #######################################################



device = 'Amazfit Band 5'
reviewlist = []
amazon = 'Amazon.com: Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.com/Amazfit-Fitness-Monitoring-Tracking-Resistant/product-reviews/B08DKYLK4D/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df1 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇺🇸',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')


reviewlist = []
amazon = 'Amazon.co.uk:Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.co.uk/Amazfit-Band-Fitness-Tracker-Waterproof/product-reviews/B08DKWSVZG/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df2 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇬🇧',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')



reviewlist = []
amazon = 'Amazon.ca:Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.ca/Amazfit-Midnight-Black-Works-Alexa/product-reviews/B08DKYLK4D/ref=cm_cr_getr_d_paging_btm_prev_5?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df3 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇨🇦',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')


device_1 = pd.concat([df1,df2,df3])



###########################################################################################################################
################################################## ANCWEAR ################################################################



device = 'ANCwear'
reviewlist = []
amazon = 'Amazon.com: Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.com/ANCwear-Activity-Exercise-Waterproof-Pedometer/product-reviews/B07YFBHRN7/ref=cm_cr_getr_d_paging_btm_next_7?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df1 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇺🇸',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')



reviewlist = []
amazon = 'Amazon.co.uk:Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.co.uk/Trackers-Activity-Waterproof-Compatible-Smartphone/product-reviews/B0823ZCMM5/ref=cm_cr_getr_d_paging_btm_next_7?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df2 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇬🇧',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')



reviewlist = []
amazon = 'Amazon.ca:Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.ca/ANCwear-Activity-Exercise-Waterproof-Pedometer/product-reviews/B07YFBHRN7/ref=cm_cr_getr_d_paging_btm_next_6?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df3 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇨🇦',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')


device_2 = pd.concat([df1,df2,df3])



###################################################################################################################################
################################################## FITBIT CHARGE 4 ################################################################



device = 'Fitbit Charge 4'
reviewlist = []
amazon = 'Amazon.com: Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.com/Fitbit-Fitness-Activity-Tracking-Included/product-reviews/B084CQ41M2/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df1 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇺🇸',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')



reviewlist = []
amazon = 'Amazon.co.uk:Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.co.uk/Fitbit-Advanced-Fitness-Tracker-Tracking/product-reviews/B084CQ41M2/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df2 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇬🇧',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')



reviewlist = []
amazon = 'Amazon.ca:Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.ca/Fitbit-Fitness-Activity-Tracking-Included/product-reviews/B084CQ41M2/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df3 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇨🇦',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')


device_3 = pd.concat([df1,df2,df3])



###########################################################################################################################
################################################## FITBIT CHARGE 5 ########################################################



device = 'Fitbit Charge 5'
reviewlist = []
amazon = 'Amazon.com: Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.com/Fitbit-Advanced-Management-Tracking-Graphite/product-reviews/B09BXQ4HMB/ref=cm_cr_getr_d_paging_btm_next_5?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df1 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇺🇸',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')



reviewlist = []
amazon = 'Amazon.co.uk:Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.co.uk/Fitbit-Activity-6-months-Membership-Readiness/product-reviews/B09BXQ4HMB/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df2 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇬🇧',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')



reviewlist = []
amazon = 'Amazon.ca:Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.ca/Advanced-Management-Tracking-Graphite-Included/product-reviews/B09CSX5G3V/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df3 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇨🇦',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')


device_4 = pd.concat([df1,df2,df3])



##################################################################################################################
################################################## FITBIT INSPIRE 2 ##############################################



device = 'Fitbit Inspire 2'
reviewlist = []
amazon = 'Amazon.com: Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.com/Fitbit-Inspire-Fitness-Tracker-Included/product-reviews/B08DFGPTSK/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df1 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇺🇸',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')


reviewlist = []
amazon = 'Amazon.co.uk:Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.co.uk/Fitbit-Inspire-Fitness-Tracker-Premium/product-reviews/B08DFGPTSK/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df2 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇬🇧',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')



reviewlist = []
amazon = 'Amazon.ca:Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.ca/Fitbit-Inspire-Fitness-Tracker-Included/product-reviews/B08FSBNJG8/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df3 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇨🇦',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')


device_5 = pd.concat([df1,df2,df3])



##################################################################################################################
################################################## GARMIN ########################################################



device = 'Garmin Vivofit 4'
reviewlist = []
amazon = 'Amazon.com: Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.com/Garmin-v%C3%ADvofit-activity-display-010-01847-00/product-reviews/B077X1SQY9/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df1 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇺🇸',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')


reviewlist = []
amazon = 'Amazon.com: Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.com/Garmin-v%C3%ADvofit-activity-display-010-01847-00/product-reviews/B077X1SQY9/ref=cm_cr_arp_d_viewopt_rvwer?ie=UTF8&reviewerType=avp_only_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df2 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇺🇸',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')



reviewlist = []
amazon = 'Amazon.co.uk:Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.co.uk/Garmin-v%C3%ADvofit-activity-display-010-01847-03/product-reviews/B077WTKG7N/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df3 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇬🇧',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')



reviewlist = []
amazon = 'Amazon.ca:Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.ca/Garmin-v%C3%ADvofit-Activity-Display-010-01847-00/product-reviews/B077X1SQY9/ref=cm_cr_getr_d_paging_btm_next_7?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df4 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇨🇦',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')


device_6 = pd.concat([df1,df2,df3,df4])



##################################################################################################################
################################################## HUAWEI ########################################################



device = 'HUAWEI Band 4 Pro'
reviewlist = []
amazon = 'Amazon.com: Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.com/HUAWEI-Band-Pro-Touchscreen-Built/product-reviews/B08179V446/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df1 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇺🇸',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')


reviewlist = []
amazon = 'Amazon.com: Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.com/HUAWEI-Band-Pro-Touchscreen-Built/product-reviews/B08179V446/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df2 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇺🇸',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')



reviewlist = []
amazon = 'Amazon.co.uk:Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.co.uk/HUAWEI-Band-Pro-Touchscreen-Built-Black/product-reviews/B08179V446/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df3 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇬🇧',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')



reviewlist = []
amazon = 'Amazon.ca:Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.ca/HUAWEI-Band-Pro-Touchscreen-Built/product-reviews/B08179V446/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df4 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇨🇦',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')


device_7 = pd.concat([df1,df2,df3,df4])



###########################################################################################################################
################################################## MOREPRO ################################################################



device = 'MorePro'
reviewlist = []
amazon = 'Amazon.com: Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.com/MorePro-Pressure-Activity-Waterproof-Smartwatch/product-reviews/B0891VTYYJ/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df1 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇺🇸',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')



reviewlist = []
amazon = 'Amazon.ca:Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.ca/MorePro-Activity-Wateproof-Smartwatch-Pedometer/product-reviews/B08MVR8LG9/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df2 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇨🇦',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')


device_8 = pd.concat([df1,df2])



###########################################################################################################################
################################################## SAMSUNG GALAXY FIT 2 ###################################################



device = 'Samsung Galaxy Fit 2'
reviewlist = []
amazon = 'Amazon.com: Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.com/Samsung-Galaxy-Bluetooth-Fitness-Tracking/product-reviews/B08H6SQTW1/ref=cm_cr_getr_d_paging_btm_next_4?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df1 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇺🇸',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')



reviewlist = []
amazon = 'Amazon.co.uk:Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.co.uk/Samsung-Galaxy-Fit-Activity-Tracker/product-reviews/B08H5MP84J/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df2 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇬🇧',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')



reviewlist = []
amazon = 'Amazon.ca:Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.ca/Advanced-Management-Tracking-Graphite-Included/product-reviews/B09CSX5G3V/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df3 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇨🇦',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')


device_9 = pd.concat([df1,df2,df3])


###########################################################################################################################
################################################## XIAOMI BAND 5 ##########################################################



device = 'Xiaomi Mi Band 5'
reviewlist = []
amazon = 'Amazon.com: Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.com/Xiaomi-Band-Wristband-Magnetic-Bluetooth/product-reviews/B089NS9JW2/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df1 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇺🇸',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')


reviewlist = []
amazon = 'Amazon.co.uk:Customer reviews: '
for x in range(1,1000):
    soup = get_soup(f'https://www.amazon.co.uk/Xiaomi-Band-Health-Fitness-Tracker/product-reviews/B089NS9JW2/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Obteniendo pagina: {x}')
    get_reviews(soup,amazon)
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break
df = pd.DataFrame(reviewlist)
df2 = df >> mutate(COUNTRY = (X.COUNTRY_DATE.str.split(' on ', 1, expand=True)[0]).str.replace(' 🇬🇧',''), DATE = pd.to_datetime(df.COUNTRY_DATE.str.split(' on ', 1, expand=True)[1]).dt.date, DEVICE = device) >> select(9,0,1,2,3,4,7,8,6) 
print('Fin')



device_10 = pd.concat([df1,df2])

##########################################################################################################################

Final = pd.concat([device_1, device_2, device_3, device_4, device_5, device_6, device_7, device_8, device_9, device_10])
Final.to_excel('FINAL.xlsx', index = None, header=True,  sheet_name = 'DATA')
