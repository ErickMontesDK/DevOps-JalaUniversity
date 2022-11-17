import virtualbox
import argparse

parser = argparse.ArgumentParser(description = 'Programm CLI')
parser.add_argument('--machines', '-m', action='store_true',)
parser.add_argument('--launch', '-l', help="Escribe el nombre de la maquina a usar" )
parser.add_argument('--create', '-c', action='store_true', )
parser.add_argument('--close', '-cls', action='store_true', )

vbox = virtualbox.VirtualBox()
listMachines=[m.name for m in vbox.machines]

def getMachines():
    print("The machines available are:")
    for machine in listMachines:
        print(machine)

def newMachine():
    m = vbox.create_machine("",sys.argv[2],['/test'],"Linux",'forceOverwrite=0')
    vbox.register_machine(m)

#def closeMachine():
#    session.console.power_down()

def launchMachine(machineName):
    session = virtualbox.Session()
    machine = vbox.find_machine(machineName)
    progress = machine.launch_vm_process(session, "gui", [])
    progress.wait_for_completion()
    print(session.state)
    print(machine.state)

if __name__ == '__main__':
    args=parser.parse_args()

    if args.machines:
        getMachines()
    elif args.launch:
        launchMachine(args.launch)  
    else:
        print("no hay opcion con -h")