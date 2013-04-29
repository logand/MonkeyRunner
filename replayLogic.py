from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys
from com.xhaus.jyson import JysonCodec as json

def run_input(action, newdevice, test):
    actionComplete = True
    if action['type'] == 'touch':
        counter = (action['up'] - action['down'])/1000
        if test:
            print 'touch at (' + str(action['x']) + ", " + str(action['y']) + ") for " + str(counter) + " seconds"
        else:
            newdevice.touch(action['x'], action['y'], 'DOWN')
            MonkeyRunner.sleep(counter)
            newdevice.touch(action['x'], action['y'], 'UP')
        
    elif action['type'] == 'drag':
        counter = action['up'] - action['down']
        strTuple = (action['points'][0]['x'], action['points'][0]['y'])
        endTuple = (action['points'][1]['x'], action['points'][1]['y'])
        if test:
            print 'drag from ' + str(strTuple) + ' to ' + str(endTuple) + ' for ' + str(counter)
        else:
            newdevice.drag(strTuple, endTuple, counter, 10)
    elif action['type'] == 'press':
        counter = action['up'] - action['down']
        times = len(action['keys'])
        #print str(times) + 'keys to press'
        if test:
            for i in range(times):
                print 'pressed %s key for %d' % (action['keys'][i]['key'], counter)
        else:
            for i in range(times):
                newdevice.press(action['keys'][i]['key'], MonkeyDevice.DOWN)
            MonkeyRunner.sleep(counter)
            for i in range(times):
                newdevice.press(action['keys'][i]['key'], MonkeyDevice.UP)
    else:
        actionComplete = False
    return actionComplete


def run_jblock(filename, newdevice):
    f = open(filename, 'r')
    print "opened file"
    totalCompleted = 0
    totalActions = 0
    newdevice.wake()
    for line in f:
        totalActions += 1
        device_input = json.loads(line)
        complete = run_input(device_input, newdevice, False)
        if complete:
            totalCompleted += 1
        else:
            action = str(device_input).replace(': u', ': ')
            print 'could not replay action ' + str(action)
    print str(totalCompleted)+ '/' + str(totalActions) + ' actions completed'

def main():
    if len(sys.argv) == 1:
        filename = 'testLogicLog.txt'
    else:
        filename = sys.argv[1]
    newdevice = MonkeyRunner.waitForConnection()  
    run_jblock(filename, newdevice)
    print 'done'

#optparse
if __name__ == '__main__':
  main()