from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.custom import Custom

with Diagram("Web Service", show=False, direction="LR"):
    AGENT = Custom("EA1", "ea.png")
    PROXY = Custom("Proxy", "proxy.png")
    TE = Custom("ThousandEyes\nPlatform", "te.png")

    AGENT >> PROXY >> TE
    ELB("lb") >> EC2("web") >> RDS("userdb")
