
# First, we import the utilities
import project_management_utils

#from project_management_utils.Disk_Jockey import Disk_Jockey
from project_management_utils.Journal import journal

import numpy as np

class John_Physics:

    # solves physics

    def __init__(self, ID, log_verbosity = 5):

        self.ID = ID # A string that identifies this instance of John_Physics. It is the "experiment's label".

        # Firstly, we initialise an instance of Journal (for logging) and Disk Jockey (for data management)

        # Verbosity tells the instance of John_Physics to ignore logs of higher verbosity than its own.
        # If you set verbosity to be low here, only important messages will be logged.
        # Of course, for every log, you can set the verbosity requirement manually.
        # A message will not be logged even if it satisfies the verbosity requirement if any of its parent
        # routines doesn't satisfy the verbosity requirement.
        # Typically, writes within subroutines are one level of verbosity higher than the subroutine itself.

        self.dj = project_management_utils.Disk_Jockey(f"outputs/{self.ID}")
        self.dj.create_data_nodes({"system" : {"log" : "txt"}})
        # Disk Jockey requires a string to identify the subdirectory where it reads and writes data. This is
        # why the ID string is very important.
        # We pass our instance of Journal to Disk Jockey, and now Disk Jockey can use it to print to the log.
        # We can start out by creating some default, static part of data node structure. Here, there will
        # always be a subfolder ".../system/", with a file "log.txt".
        # More elements can be added to the node structure at any point: for example, each dataset can have
        # its own subfolder if it comes with multiple datafiles! Disk Jockey will read the actual node
        # structure on load from its root metadata file.
        # Note that all metadata files are by default .json except if the datafile is a .csv, in which case
        # the metadata has to be .pkl in order to store the column types. .pkl is very versatile, but .json
        # is human-readable. You can specify metadata filetypes by calling set_metadatum_type.

        self.string_solutions = {} # [dataset name] = solution

    def solve_string_theory(self, number_of_strings):

        journal.enter(f"Solving string theory with {number_of_strings} strings", 0)
        # Here we tell the Journal that we entered a new routine. All subsequent logs will be marked as
        # children of this routine until the exit method is called.

        journal.write("Time to tie up some strings!", 5)
        # This message has verbosity 5, so it only logs if you set verbosity to 5 or higher!

        journal.write("Asking mooses for help", 1)
        # Time to enter a child routine and see what happens!
        self.enumerate_moose_friendship(12)

        journal.write("Time to think really hard!", 1)
        # Here we show how powerful Sempahors are to log long processes. They update at user-specified
        # intervals and always estimate how long will it take for the process to finish. To start a semaphor
        # process, just use Journal.enter and pass semaphored = True together with the required kwargs.

        semaphor_msg = "Thinking about stringy cheese"
        # Every semaphor process has a header, so you don't forget what is the think eating your RAM.

        simulation_time_checkpoints = (number_of_strings * number_of_strings, 50)
        # Semaphor processes are measured in simulation time, which can be any parameter you choose.
        # Sim time always starts at 0 and finishes at some provided value tau_max. When initialising
        # a semaphor event, you can pass as tau_space either a single number--the value of tau_max--or
        # a tuple (tau_max, N_divisions). In the first case, N_divisions defaults to 1000. The purpose
        # is to save time on frequent updates by only refreshing the printed output when sim time goes
        # from one division to another.
        # In case you pass update_on_every_tick = True, N_divisions is ignored, as the printed output
        # updates on every semaphor event update.

        sem_ID = journal.enter(semaphor_msg, 1, semaphored = True, label = 'Cheese', tau_space = simulation_time_checkpoints)
        # The naming convention is that tau stands for simulation time and t stands for real time.

        result = np.zeros((number_of_strings, number_of_strings))

        for a in range(number_of_strings):
            for b in range(number_of_strings):
                # We do something very computationally heavy here, I think

                total = 0
                for i in range(1000):
                    for j in range(1000):
                        total += ((i + a) * (j + b)) % 97

                result[a][b] = total

                journal.semaphor_progress(1)
                # Don't forget to update the semaphor with the current sim time!

        duration = journal.exit()
        # By exiting we close the Semaphor process. This exit uniquely returns a value:
        # the duration of the process measured in seconds, as a float.

        # Note that we can still print to output inside a semaphored routine, and we can nest
        # semaphored routines. Here is an example:

        mod_widths = np.arange(107, 893, 91, dtype = int)
        N_churns = 1000000

        sem_A = journal.enter("Testing modular curds", 1, semaphored = True, label = 'Curds', tau_space = (len(mod_widths) * N_churns, len(mod_widths) * 3))


        for mod_width_i in range(len(mod_widths)):
            mod_width = mod_widths[mod_width_i]
            x = 0
            magical_curds = 0

            sem_B = journal.enter(f"Testing curd made by {mod_width} cheesemakers", 1, semaphored = True, label = 'Mod ' + str(mod_width), tau_space = N_churns, c = 'yellow', width = 27)

            for a in range(N_churns):
                x = (x * x * mod_width + magical_curds + 2 ** (a % 15) + mod_width * mod_width) % 100
                if x == 87:
                    journal.warning("Magical curd found!")
                    magical_curds += 1
                if x == 0:
                    journal.write("Cyclic curd found! Terminating early.")
                    break
                journal.semaphor_progress(S_ID = sem_A)
                journal.semaphor_progress(S_ID = sem_B)
            journal.exit()
            journal.semaphor_update((mod_width_i + 1) * N_churns, S_ID = sem_A)
        journal.exit()

        # Finally, let's discuss Semaphor overtime. In processes where the computation may
        # arbitrarily prolong, we can call overtime(tau_overtime), which means we progressed
        # tau by tau_overtime, which also has to be added to tau_max.

        min_tries = 20

        max_tries = 60

        journal.write("Gerard 't Hooft hypothesis considered! Dutch cheese constructed.")
        _ = journal.enter("Waiting for Goudot", semaphored = True, label = 'Goudot', tau_space = 10 * min_tries)

        i = 0
        maximal_guess = 0
        N_hoofts = 300000
        for i in range(10):

            journal.write(f"Goudot roll number: {i + 1}")

            found_better_val = False

            for j in range(min_tries):

                cur_best_guess = 100000
                for b in range(2):
                    x = i * max_tries + j * 2 + b
                    for a in range(N_hoofts):
                        x = (1664525 * x + 1013904223) % 2**32
                    x = x % 100000
                    if x < cur_best_guess:
                        cur_best_guess = x
                if cur_best_guess > maximal_guess:
                    maximal_guess = cur_best_guess
                    found_better_val = True
                    journal.write(f"Better guess found: {maximal_guess}")
                    journal.semaphor_progress(min_tries - j)
                    break
                journal.semaphor_progress()

            if not found_better_val:
                journal.warning("Entering overtime")

            while (j < max_tries and (not found_better_val)):
                cur_best_guess = 100000
                for b in range(2):
                    x = i * max_tries + j * 2 + b
                    for a in range(N_hoofts):
                        x = (1664525 * x + 1013904223) % 2**32
                    x = x % 100000
                    if x < cur_best_guess:
                        cur_best_guess = x
                if cur_best_guess > maximal_guess:
                    maximal_guess = cur_best_guess
                    found_better_val = True
                    journal.write(f"Better guess found: {maximal_guess}")
                    break
                journal.semaphor_overtime()
                j += 1

        journal.exit()

        journal.write(f"Best guess for the size of Gerard 't Hooft's cheese wheel: {maximal_guess}")



        # Now, let us pass the result onto Disk Jockey. Let's create a new data node:
        data_group_name = f"{number_of_strings}_strings"
        self.dj.create_data_nodes({data_group_name : {"result" : "json"}})
        # The data group name should be unique: here I'm playing a dangerous game. Do better than this!

        # Now, let us store the data:
        self.dj.commit_datum_bulk(data_group_name, "result", result.tolist())
        self.dj.commit_metadatum(data_group_name, "result", {"duration" : duration})
        # The actual file is going to be a .txt, so string conversion it is. The metadata file is a .json,
        # and we can add datapoints to it until the point of writing to disk (which comes later!)

        # We should also store them internally for analysis, plotting etc.
        self.string_solutions[data_group_name] = result

        journal.exit()


    def enumerate_moose_friendship(self, number_of_mooses, current_friendship = 1):
        # It is well known that two mooses meeting must be but fleeting, but when three mooses meet, they
        # stop and greet. This method uses tail recursion to calculate how many friendly greetings occur.

        journal.enter(f"Calculating moose friendship with {number_of_mooses} mooses remaining", 5)
        # Because the method is recursive, logging from inside can repeat many times. Better set the
        # verbosity to be high!

        if number_of_mooses == 0:
            journal.write("No more mooses!")
            journal.exit("End of tail!") # exit logs can have messages, too!
            return(current_friendship)
            # Make sure to firstly exit the routine in Journal, and only then terminate!

        magnified_friendship = self.enumerate_moose_friendship(number_of_mooses - 1, number_of_mooses + current_friendship)
        journal.exit()
        return(magnified_friendship)

    def print_string_solutions(self):
        # A cheeky output function. Pretend these are nice plots and whatnot.
        journal.enter("Printing calculated solutions")
        for dataset_label, dataset_value in self.string_solutions.items():
            journal.write(f"Result for dataset '{dataset_label}': {np.sum(dataset_value)}")
        journal.exit()

    def save_data(self):
        # Here we tell Disk Jockey to save the committed data to disk

        self.dj.commit_datum_bulk("system", "log", journal.dump())
        # First, we commit the current state of the Journal. Note that the internal dump looks a bit
        # different to what's in your terminal, with no fancy printing or Semaphor artifacts.
        self.dj.commit_metadatum_point("system", "log", "datasets", list(self.string_solutions.keys()))
        # We can add to existing metadata values datapoint by datapoint.

        self.dj.save_data()
        # We can specify which data groups to save, or save them all!

    def load_data(self):
        # Here, we simply tell Disk Jockey to load data from disk. Because it took notes last time, it now
        # knows exactly what files to load.

        journal.enter("Loading data", 0)

        self.dj.load_data()
        # Once again, we can restrict ourselves to loading only particular data groups. This can be very
        # useful: for example, I work on a script for computational chemistry, and sometimes I want to load
        # the calculated molecule properties without loading my old datasets, so I don't have to wait for the
        # program to perform costly calculation on the same molecule again. And those old datasets will wait
        # for me on the disk until I need to compare them to the new ones at any later point!

        # Of course, we still need to access the data. Let's save it to some internal property here.
        for dataset_label in self.dj.metadata["system"]["log"]["datasets"]:
            journal.write(f"Restoring dataset {dataset_label}", 3)
            self.string_solutions[dataset_label] = np.array(self.dj.data_bulks[dataset_label]["result"])
        # As you can see, you still need to know the structure of the data in order to be able to interpret
        # it. With great freedom comes great flexibility!

        journal.exit()


def saving_example():
    journal.set_verbosity(5)
    journal.set_max_row_width(37)

    john = John_Physics("example")
    john.solve_string_theory(12)
    john.print_string_solutions()
    john.save_data()
    journal.close_journal()
    # This de-buffers the highlighted row and prints out a dinkus. It would be better to have it automated in
    # some teardown routine of John_Physics!

def loading_example():
    journal.set_verbosity(5)

    john = John_Physics("example")
    john.load_data()
    john.solve_string_theory(10)
    # After loading old data, we can still add new data. Saving at the end stores both!
    john.print_string_solutions()
    john.save_data()
    journal.close_journal()

# To see how this example works, firstly run the saving_example() function. Then, go see the contents of the
# outputs/ subdirectory which will be created. Then, comment out the saving_example() call and instead run
# the loading_example() function. Enjoy!

saving_example()
#loading_example()


