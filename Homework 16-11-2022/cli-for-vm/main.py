import virtualbox
import argparse

parser = argparse.ArgumentParser(description = 'Programm CLI')
parser.add_argument('--machines', '-m', action='store_true',)
parser.add_argument('--launch', '-l', help="Escribe el nombre de la maquina a usar" )
parser.add_argument('--create', '-c', )
parser.add_argument('--close', '-cls', action='store_true', )
parser.add_argument('--delete', '-d', help="Escribe el nombre de la maquina a borrar" )

vbox = virtualbox.VirtualBox()
listMachines=[m.name for m in vbox.machines]

def getMachines():
    print("The machines available are:")
    for machine in listMachines:
        print(machine)

def newMachine(newMachine):
    m = vbox.create_machine("",newMachine,['/'],"",'')
    vbox.register_machine(m)

def closeMachine():
    session.console.power_down()

def deleteMachine(machine_to_delete):
    dm = vbox.find_machine(machine_to_delete)
    dm.remove(delete=True)

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
    elif args.close:
        closeMachine()
    elif args.launch:
        launchMachine(args.launch)  
    elif args.create:
        newMachine(args.create) 
    elif args.deleteMachine:
        deleteMachine(args.deleteMachine) 
    else:
        print("no hay opcion con ese msg -h")