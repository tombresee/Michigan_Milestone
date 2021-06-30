

Tom Bresee - Michigan Milestone - Data Science 
##################################################


|
|


:Authors: Tom Bresee
:University: Michigan
:HPC: Great Lakes
:Hadoop:  ?
:Mark:  I
:URL:  https://tom-bresee.herokuapp.com/





|
|




Accessing Great Lakes via Browser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  VPN in to U of M
2.  https://greatlakes.arc-ts.umich.edu/pun/sys/dashboard
3.  Click url for connectivity (top)
4.  Can also ssh directly to that url if you want...



|
|




LinkedIn Learning (U of Michigan)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* https://www.linkedin.com/learning/me?u=42573940



|
|


Great Lakes Advanced 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* https://docs.google.com/presentation/d/1BSVBvok47JLc0imlvTnG3Mt_Wh_sfA-hb9j0Q_0XSyQ/edit#slide=id.p11



|
|



THUNDER-X
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `ThunderX Main Page <https://arc.umich.edu/cavium/>`_ 
* `Using Cavium <https://arc.umich.edu/cavium/user-guide/>`_ 
* ssh cavium-thunderx.arc-ts.umich.edu
* `Hadoop Base Commands <http://hadoop.apache.org/docs/r2.5.2/hadoop-project-dist/hadoop-common/FileSystemShell.html>`_  
* University of Michigan ARC-TS spark examples:  https://bitbucket.org/umarcts/spark-examples/src/master/
* https://bitbucket.org/umarcts/spark-examples/src/master/
* U of M Bitbucket from ARC-TS:  https://bitbucket.org/umarcts/
* Big Data Research PPT:  https://umarcts.bitbucket.io/presentations/hadoop/#/title
* Do these commands from the thunderX user guide: https://arc.umich.edu/cavium/user-guide/



|
|


Links
~~~~~~~~~~~~~~~~~~~~~
* https://greatlakes.arc-ts.umich.edu/pun/sys/dashboard
* https://arc.umich.edu/greatlakes/user-guide/
* https://arc.umich.edu/greatlakes/software/tensorflow/
* https://arc.umich.edu/systems-services/ybrc-pipeline/
* https://arc.umich.edu/systems-services/ybrc-pipeline/
* http://www-personal.umich.edu/~tbresee/
* https://arc.umich.edu/greatlakes/user-guide/#document-5
* https://arc.umich.edu/greatlakes/configuration/
* https://app.globus.org/file-manager/collections/68512a70-d476-11eb-9b44-47c0f9282fb8/overview
* https://app.globus.org/file-manager?origin_id=68512a70-d476-11eb-9b44-47c0f9282fb8&origin_path=%2F~%2F
* https://auth.globus.org/v2/web/logout?client_id=89ba3e72-768f-4ddb-952d-e0bb7305e2c7&redirect_uri=https%3A%2F%2Fapp.globus.org&redirect_name=Globus%20Web%20App%20log%20in&viewlocale=en_US
* `All Physical Code from pg4e com <https://www.pg4e.com/code/>`_
* `All Physical Lectures from pg4e com <https://www.pg4e.com/lectures/>`_
* `Lecture Notes 1 <https://www.pg4e.com/lectures/05-FullText>`_
* https://www.mivideo.it.umich.edu/media/t/1_rpw9zxi2/181860561
* https://greatlakes.arc-ts.umich.edu/pun/sys/dashboard
* http://www-personal.umich.edu/~cja/
* https://arc.umich.edu/event/introduction-research-computing-on-the-great-lakes-cluster-4-2/


|
|


Notes
~~~~~~~~~~~~~~~~~~~~~
MPI research
MPI program needs to be started 
how many ranks do you want ? 
four sep copies of python in their own slurm tasks
sep nodes 
single computation run across multiple nodes 




[tbresee@gl-login2 ~]$ cp -ar /sw/examples/workshops/hpc201 ~
[tbresee@gl-login2 ~]$ cd ~/hpc201/hpc-201-cpu/arrayjob




[tbresee@gl-login2 arrayjob]$ ls -la
total 328
drwxrwxr-x  5 tbresee tbresee 109 Jan 30  2020 .
drwxrwxr-x 17 tbresee tbresee 379 Feb  4 12:52 ..
drwxrwxr-x  2 tbresee tbresee  26 Jan 30  2020 1
drwxrwxr-x  2 tbresee tbresee  26 Jan 30  2020 2
drwxrwxr-x  2 tbresee tbresee  26 Jan 30  2020 3
-rw-rw-r--  1 tbresee tbresee 316 Jun  7  2019 arr.m
-rwxrwxr-x  1 tbresee tbresee 161 Jan 16  2020 submit.sbat
[tbresee@gl-login2 arrayjob]$
[tbresee@gl-login2 arrayjob]$
[tbresee@gl-login2 arrayjob]$
[tbresee@gl-login2 arrayjob]$
[tbresee@gl-login2 arrayjob]$
[tbresee@gl-login2 arrayjob]$
[tbresee@gl-login2 arrayjob]$ cat arr.m
% hpc201

% change to this array job element's working directory
mydir = getenv('SLURM_ARRAY_TASK_ID');
cd(mydir);
disp(pwd)

% read seed and initialize generator
seed = textread('seed.txt', '%d');
rng(seed)

% compute and display product of two random matrices
A = rand(4);
B = rand(4);
C = A*B
save('output','C');






--- burn core for 30s ----


[tbresee@gl-login2 python-example]$ cat burn-mpi.py
# run with 'mpirun [-np 4] python print_rank.py"

from mpi4py import MPI
import sys
import os

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

print("Process %d of %d on %s begins.\n" % (rank, size, name))
os.system(r'~cja/glbin/burn -s30')
print("Process %d of %d on %s terminated.\n" % (rank, size, name))






[tbresee@gl-login2 python-example]$ sq
             JOBID PARTITION     NAME     USER  ACCOUNT ST       TIME  NODES NODELIST(REASON)






sbatch -account=training submit.sbat



[tbresee@gl-login2 arrayjob]$ sbatch submit.sbat
Submitted batch job 21756876


[tbresee@gl-login2 arrayjob]$ sq
             JOBID PARTITION     NAME     USER  ACCOUNT ST       TIME  NODES NODELIST(REASON)
        21756876_1  standard      arr  tbresee training  R       0:09      1 gl3055
        21756876_2  standard      arr  tbresee training  R       0:09      1 gl3056
        21756876_3  standard      arr  tbresee training  R       0:09      1 gl3156










[tbresee@gl-login2 arrayjob]$ sbatch submit.sbat
Submitted batch job 21757879


[tbresee@gl-login2 arrayjob]$ sq
             JOBID PARTITION     NAME     USER  ACCOUNT ST       TIME  NODES NODELIST(REASON)
        21757879_1  standard      arr  tbresee training  R       0:00      1 gl3077
        21757879_2  standard      arr  tbresee training  R       0:00      1 gl3156
        21757879_3  standard      arr  tbresee training  R       0:00      1 gl3049




[tbresee@gl-login2 arrayjob]$ my_accounts
   Cluster                        Account                        GrpTRES   GrpTRESMins MaxJobs       MaxTRES MaxSubmit     MaxWall                  QOS
---------- ------------------------------ ------------------------------ ------------- ------- ------------- --------- ----------- --------------------
greatlakes                       training                                                                         5000    01:00:00             training










[tbresee@gl-login2 python-example]$ sq
             JOBID PARTITION     NAME     USER  ACCOUNT ST       TIME  NODES NODELIST(REASON)


[tbresee@gl-login2 python-example]$ sbatch burn-mpi.sbat
Submitted batch job 21759034


[tbresee@gl-login2 python-example]$ sq
             JOBID PARTITION     NAME     USER  ACCOUNT ST       TIME  NODES NODELIST(REASON)
          21759034  standard burn-mpi  tbresee training PD       0:00      1 (None)


[tbresee@gl-login2 python-example]$ ll
total 704
-rw-rw-r-- 1 tbresee tbresee   360 Oct  9  2020 burn-mpi.py
-rwxrwxr-x 1 tbresee tbresee   221 Jun 23 21:20 burn-mpi.sbat
-rwxrwxr-x 1 tbresee tbresee 12792 Oct  9  2020 cpi16
-rw-r--r-- 1 tbresee tbresee  2162 Oct  9  2020 cpi16.c
-rw-rw-r-- 1 tbresee tbresee  1232 Oct  9  2020 doubler.py
-rw-rw-r-- 1 tbresee tbresee  1131 Oct  9  2020 ppi.py
-rwxrwxr-x 1 tbresee tbresee  1804 Sep 28  2017 print_rank.pbs
-rw-rw-r-- 1 tbresee tbresee   259 Sep 20  2015 print_rank.py
-rwxrwxr-x 1 tbresee tbresee   226 Jun 23 21:20 print_rank.sbat
-rw-rw-r-- 1 tbresee tbresee   248 Jun 24 11:32 slurm-21758952.out
-rw-rw-r-- 1 tbresee tbresee     0 Jun 24 11:36 slurm-21759034.out


[tbresee@gl-login2 python-example]$ cat slurm-21759034.out

Process 0 of 4 on gl3036.arc-ts.umich.edu begins.

Process 1 of 4 on gl3036.arc-ts.umich.edu begins.

Process 2 of 4 on gl3036.arc-ts.umich.edu begins.

Process 3 of 4 on gl3036.arc-ts.umich.edu begins.

burn:  burning for 30 sec on 1 threads with 1 GB 0% resident memory
burn:  burning for 30 sec on 1 threads with 1 GB 0% resident memory
burn:  burning for 30 sec on 1 threads with 1 GB 0% resident memory
burn:  burning for 30 sec on 1 threads with 1 GB 0% resident memory







[tbresee@gl-login2 launcher]$ sbatch submit.sbat
Submitted batch job 21759140

[tbresee@gl-login2 launcher]$ sq
             JOBID PARTITION     NAME     USER  ACCOUNT ST       TIME  NODES NODELIST(REASON)
          21759140  standard launcher  tbresee training  R       0:00      2 gl[3071-3072]

[tbresee@gl-login2 launcher]$ ll
total 408
drwxrwxr-x 2 tbresee tbresee  26 Jan 30  2020 1
drwxrwxr-x 2 tbresee tbresee  26 Jan 30  2020 2
drwxrwxr-x 2 tbresee tbresee  26 Jan 30  2020 3
-rw-rw-r-- 1 tbresee tbresee 309 Jan 30  2020 arr.m
-rw-rw-r-- 1 tbresee tbresee   0 Jun 24 11:39 job_1.out
-rw-rw-r-- 1 tbresee tbresee   0 Jun 24 11:39 job_3.out
-rw-rw-r-- 1 tbresee tbresee 144 Jan 30  2020 jobfile
-rw-rw-r-- 1 tbresee tbresee 504 Jun 24 11:39 slurm-21759140.out
-rwxrwxr-x 1 tbresee tbresee 327 Jan 30  2020 submit.sbat

[tbresee@gl-login2 launcher]$ cat slurm-21759140.out
Launcher version 3.5 loaded. For help, type: ml help launcher
Launcher: Setup complete.

------------- SUMMARY ---------------
   Number of hosts:    2
   Working directory:  /home/tbresee/hpc201/hpc-201-cpu/launcher
   Processes per host: 1
   Total processes:    2
   Total jobs:         3
   Scheduling method:  block

-------------------------------------

Launcher: Starting parallel tasks...

using /tmp/launcher.21759140.hostlist.TXK62qsz to get hosts

starting job on gl3071

starting job on gl3072









