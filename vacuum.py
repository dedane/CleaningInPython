import random
class Environment(object):
    def __init__(self):
       self.locationCondition ={'A':'0','B':'0'}
       self.locationCondition['A'] = random.randint(0,1)
       self.locationCondition['B'] = random.randint(0,1)

class SimpleReflexVacuumAgent(Environment):
    def __init__(self,Environment):
        print(Environment.locationCondition)

        Score = 0
        vacuumLocation =random.randint(0,1)

        if vacuumLocation == 0:
            print('Vacuum is randomly placed at Location A')

            if Environment.locationCondition['A'] == 1:
                print('Location A is Dirty.')

            Environment.locationCondition['A'] = 0
            print('Location A has been cleaned.')

            print('Moving to location B.....')

            if Environment.locationCondition['B'] == 1:
                print('Location B is Dirty')

                Environment.locationCondition['B'] = 0;
                print('Location B is dirty.')

            else:
                print('Moving to location B....')

                if  Environment.locationCondition['B'] == 1:
                    print('Location B is Dirty.')

                    Environment.locationCondition['B'] = 0;
                    print('Location B has been Cleaned.')

        elif vacuumLocation == 1:
            print('Vacuum is randomly placed at Location B')

            if Environment.locationCondition['B'] == 1:
                print('Location A is Dirty.')

                Environment.locationCondition['B'] = 0;
                print('Location A has been cleaned.')

                print('Moving to location A.....')

                if Environment.locationCondition['A'] == 1:
                    print('Location A is Dirty')

                    Environment.locationCondition['A'] = 0;
                    print('Location A is dirty.')

            else:
                print('Moving to location A....')

                if Environment.locationCondition['A'] == 1:
                    print('Location A is Dirty.')

                    Environment.locationCondition['A'] = 0;
                    print('Location A has been Cleaned.')

        print(Environment.locationCondition)

theEnvironment = Environment()
theVacuum = SimpleReflexVacuumAgent(theEnvironment)

