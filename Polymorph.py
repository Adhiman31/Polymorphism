import logging
logging.basicConfig(filename ="poly.log",level=logging.DEBUG ,format="%(levelname)s %(asctime)s %(message)s")

class ibm:

    def courses(self):
        try:
            logging.info("this function shows  the course under IBM")
        except Exception as e:
            logging.error(e)

    def jobs(self):
        try:
            logging.info("this function shows jobs under IBM")
        except Exception as e:
            logging.error(e)

class ineuron :

    def courses(self):
        try:
            logging.info("this function shows  the course under Ineuron")
        except Exception as e:
            logging.error(e)

    def jobs(self):
        try:
            logging.info("this function shows jobs under Ineuron")
        except Exception as e:
            logging.error(e)

# making a common interface function

def interface1(k):
    k.courses()

def interface2(j):
    j.jobs()




logging.info("creating objects")
i = ibm()
ir = ineuron()

logging.info("using common interface function to pass the objects")
interface1(i)
interface1(ir)

interface2(i)
interface2(ir)







