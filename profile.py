import geni.portal as portal
import geni.rspec.pg as pg
import geni.rspec.igext as IG

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

tourDescription = \
"""
This profile provides the template for a full research cluster with head node, scheduler, compute nodes, and shared file systems.
At the moment, we start with a single node running MPI.
"""

# Setup the Tour info with the above description and instructions.  
tour = IG.Tour()
tour.Description(IG.Tour.TEXT,tourDescription)
request.addTour(tour)

node = request.XenVM("compute-node")
node.cores = 4
node.ram = 4096
    
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
node.routable_control_ip = "true"

node.addService(pg.Execute(shell="sh", command="sudo chmod 755 /local/repository/install_mpi.sh"))
node.addService(pg.Execute(shell="sh", command="sudo /local/repository/install_mpi.sh"))
  
# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)

