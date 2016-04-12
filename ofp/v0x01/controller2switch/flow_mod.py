"""Modifications to the flow table from the controller"""

# System imports
import enum

# Third-party imports

# Local source tree imports
from common import action
from common import flow_match
from common import header as of_header
from foundation import base
from foundation import basic_types


# Enums

class FlowModCommand(enum.Enum):
    """
    List the possible commands for a flow.

    Enums:
        OFPFC_ADD               # New Flow
        OFPFC_MODIFY            # Modify all flows
        OFPFC_MODIFY_STRICT     # Modify entry strictly matching wildcards
        OFPFC_DELETE            # Delete all matching flows
        OFPFC_DELETE_STRICT     # Strictly match wildcards and priority
    """
    OFPFC_ADD = 1
    OFPFC_MODIFY = 2
    OFPFC_MODIFY_STRICT = 3
    OFPFC_DELETE = 4
    OFPFC_DELETE_STRICT = 5


# Classes


class FlowMod(base.GenericStruct):
    """
    Modifies the flow table from the controller.

        :param header -- OpenFlow header
        :param match -- Fields to match
        :param cookie -- Opaque controller-issued identifier
        :param command -- One of OFPFC_*
        :param idle_timeout -- Idle time before discarding (seconds)
        :param hard_timeout -- Max time before discarding (seconds)
        :param priority -- Priority level of flow entry
        :param buffer_idle -- Buffered packet to apply to (or -1).
                              Not meaningful for OFPFC_DELETE*
        :param out_port -- For OFPFC_DELETE* commands, require matching
                           entries to include this as an output port.
                           A value of OFPP_NONE indicates no restriction.
        :param flags -- One of OFPFF_*
        :param actions -- The action length is inferred from the length field
                          in the header
    """
    header = of_header.OFPHeader()
    match = flow_match.OFPMatch()
    cookie = basic_types.UBInt64()
    command = basic_types.UBInt16()
    idle_timeout = basic_types.UBInt16()
    hard_timeout = basic_types.UBInt16()
    priority = basic_types.UBInt16()
    buffer_id = basic_types.UBInt32()
    out_port = basic_types.UBInt16()
    flags = basic_types.UBInt16()
    actions = action.ActionHeader()

    def __init__(self, command=None, idle_timeout=None, hard_timeout=None,
                 priority=None, buffer_id=None, out_port=None, flags=None,
                 actions=None):

        self.command=command
        self.idle_timeout=idle_timeout
        self.hard_timeout=hard_timeout
        self.priority=priority
        self.buffer_id=buffer_id
        self.out_port=out_port
        self.flags=flags
        self.actions=actions
