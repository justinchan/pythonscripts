import mechanize
import random

def main():
    for x in range (1,1000):
        br = mechanize.Browser()
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        c = random.randint(1, 100)
        d = random.randint(1, 100)
        br.addheaders = [("X-Forwarded-For", str(a) + "." + str(b) + "." + str(c) + "." + str(d))]
        br.open('http://www.surveymonkey.com/s/9BVFDJH') # survey to test
        m = br.select_form(nr=0)
        br.find_control("input_552205631_20_6419971366_0").items[0].selected = True
        # br.find_control("input_544374252_22_6331005633_0").items[0].selected = True
        # br.find_control("input_544374252_22_6331005635_0").items[0].selected = True
        # br.form.set_value("Statue of Wonjun", name='text_544374252_6331005628')
        # br.form.set_value(["6332039619_0"],name='input_544460584_10_0_0')
        # br.form.set_value(["6324206246_0"],name='input_543757558_10_0_0')
        # br.form.set_value(["6324206688_0"],name='input_543752723_10_0_0')
        # br.form.set_value(["6324225103_0"],name='input_543765829_10_0_0')
        # br.form.set_value(["6324208422_0"],name='input_543760033_10_0_0')
        # br.form.set_value(["6324209133_0"],name='input_543763795_10_0_0')
        br.submit()
        # br.response().read()#print the response
        # print br.response().read()
        print x
    print 'done'

if __name__ == "__main__":
    main()


