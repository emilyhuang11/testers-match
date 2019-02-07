




import pandas as pd

class Simulation:
    def generateData(self):
        dataFolder =''
        testers = pd.read_csv(dataFolder+'testers.csv')
        testers.dropna(inplace=True)
        tester_device = pd.read_csv(dataFolder+'tester_device.csv')
        tester_device.dropna(inplace=True)
        devices =  pd.read_csv(dataFolder+'devices.csv')
        devices.dropna(inplace=True)
        bugs = pd.read_csv(dataFolder+'bugs.csv')

        for i in range(100, 101):
            data = {'testerId':i,'firstName':'f'+str(i),   'lastName':'l'+str(i),   'country': str(i%20), 'lastLogin':i}    
            testers = testers.append(data, ignore_index=True)
            for j in range(1, 10):
                data = {'bugId':i,'testId':i, 'deviceId':j}  
                bugs = bugs.append(data, ignore_index=True)
        testers.to_csv('generated_testers.csv', encoding='utf-8', index=False)
        bugs.to_csv('generated_bugs.csv', encoding='utf-8', index=False)
        
        self.data = testers.merge(tester_device, on='testerId')
        self.data = self.data.merge(devices, on='deviceId')
        self.data = self.data.merge(bugs, on=['deviceId', 'testerId'], how = 'left')
        self.data.set_index(['country', 'description'])
        return self.data

if __name__ == '__main__':
    app = Simulation()
    app.generateData()
