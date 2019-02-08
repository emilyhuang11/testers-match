
import pandas as pd

class TestersMatchDB:
    def loadData(self, blockSize):
        self.dataFolder = input('Please input data folder:')
        testers = pd.read_csv(self.dataFolder+'/testers.csv')
        testers.dropna(inplace=True)
        self.allCountries = testers['country'].unique()
        tester_device = pd.read_csv(self.dataFolder+'/tester_device.csv')
        tester_device.dropna(inplace=True)
        devices =  pd.read_csv(self.dataFolder+'/devices.csv')
        devices.dropna(inplace=True)
        self.allDevices = devices['description'].unique()
        bugs = pd.read_csv(self.dataFolder+'/bugs.csv')
        bugs.dropna(inplace=True)
        
        # creaet a intermediate data frame that contains country, firstname, last name, description, and bugcount(nubmer of the bugs found)
        self.refinedData = pd.DataFrame(columns=['country', 'firstName', 'lastName', 'description', 'bugCount'])

        for i in range(0, testers.shape[0]//blockSize + 1):
            tempTesters = testers.iloc[(i*blockSize):((i+1)*blockSize)]
            tempData = tempTesters.merge(tester_device, on='testerId')
            tempData = tempData.merge(devices, on='deviceId')
            tempData = tempData.merge(bugs, on=['deviceId', 'testerId'], how = 'left')
            tempData = tempData[['country', 'firstName', 'lastName', 'description', 'bugId']].groupby(['country', 'firstName', 'lastName', 'description']).size().rename('bugCount').reset_index()
            self.refinedData = pd.concat([self.refinedData, tempData], sort=True)
        
        self.refinedData.set_index(['country', 'description'])
        return self.refinedData
    
    def queryData(self):
        countryDF = pd.DataFrame({'country':self.countries})
        deviceDF = pd.DataFrame({'description':self.devices})

        # convert columns country and descripiton to lower cases so that the merge is case insentive
        countryDF['country'] = countryDF['country'].str.lower()
        self.refinedData['country'] = self.refinedData['country'].str.lower()
        deviceDF['description'] = deviceDF['description'].str.lower()
        self.refinedData['description'] = self.refinedData['description'].str.lower()

        self.result = self.refinedData.merge(countryDF)
        self.result = self.result.merge(deviceDF)
        return self.result
    
    def printResult(self):
        if self.result.empty:
            print('System could not locate matching testers from the record')
        else:
            output=self.result[['firstName', 'lastName', 'bugCount']].groupby(['firstName', 'lastName']).sum().reset_index()
            output['name'] = output['firstName'] + ' ' + output['lastName']
            print(output[['name', 'bugCount']].sort_values(by='bugCount', ascending=False))
    
    def userInput(self):
        countries = input('Country List (%s,ALL. separate by \',\'):'%','.join(self.allCountries))
        if countries.upper() == 'ALL':
            self.countries = self.refinedData['country'].unique()
        else:
            self.countries = countries.replace(' ', '').split(',')
        devices = input('Device list (%s,ALL. separeate by \',\'):'%','.join(self.allDevices))
        if devices.upper() == 'ALL':
            self.devices = self.refinedData['description'].unique()
        else:
            self.devices = devices.strip().split(',')

if __name__ == '__main__':
    app = TestersMatchDB()
    app.loadData(blockSize=1000)
    app.userInput()
    app.queryData()
    app.printResult()
