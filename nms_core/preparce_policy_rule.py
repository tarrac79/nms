from enum import Enum
from nms_core.models.policyrule import PolicyRuleCheck, PolicyRuleAction


class ActionPolitic(Enum):
    ACT_DROP_PACKET = 17
    ACT_SET_QUEUE = 18
    ACT_SET_TS_CHANNEL = 19
    ACT_DISABLE_TCP_ACCEL = 20
    ACT_COMPRESS_RTP_HEADERS = 21
    ACT_DISABLE_SCREENING = 22
    ACT_SET_ACM_CHANNEL = 23
    ACT_DROP_IF_STATION_DOWN = 25
    ACT_ENCRYPT_WITH_KEY = 26
    ACT_SET_TOS = 27
    ACT_SET_DSCP = 28
    ACT_GOTO_POLICY = 29
    ACT_CALL_POLICY = 30
    ACT_COMPRESS_GTP_U = 31


class CheckPolitic(Enum):
    CHT_802_1Q_PRIORITY = 1
    CHT_VLAN_NUMBER = 2
    CHT_TOS = 3
    CHT_DSCP = 4
    CHT_PROTOCOL = 5
    CHT_SOURCE_IP_NETWORK = 6
    CHT_DESTINATION_IP_NETWORK = 7
    CHT_SOURCE_TCP_PORT = 8
    CHT_DESTINATION_TCP_PORT = 9
    CHT_SOURCE_UDP_PORT = 10
    CHT_DESTINATION_UDP_PORT = 11
    CHT_ICMP_TYPE = 12
    CHT_IP_PRECEDENCE_TYPE = 13

class Action(Enum):
    CHECK = 0
    ACTION = 1

def pre_policy(policy: PolicyRuleAction):
    policy.action_type = ActionPolitic(int(policy.action_type)).name
    policy.check_type = CheckPolitic(int(policy.check_type)).name
    policy.action = Action(int(policy.action)).name
    return policy


if __name__ == '__main__':
    pol = PolicyRuleCheck(order_num=10, type=9, invert='0', flag=0, from_=1, to=1, flag_invert=0, equal=0, enc_num=1, set_tos=0, set_dscp=0, ip_address='0.0.0.0', mask=0, id=37707, policy_id=426, action=0, value1='1', value2='1', ts_queue='0', action_type='17', flag_last_action='0', flag_last_check='0', call_policy='0', goto_policy='0', acm_channel='0', ts_stream='0', protocol_type='0', check_type='9')


    print(pre_policy(pol).to_string())
    # print(ActionPolitic(17).name)