"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'execute_program_1' block
    execute_program_1(container=container)

    return

def scan_network_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('scan_network_1() called')
    
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'scan_network_1' call

    parameters = []
    
    # build parameters list for 'scan_network_1' call
    parameters.append({
        'portlist': "",
        'script-args': "-A",
        'script': "",
        'ip_hostname': "10.10.10.161",
        'udp_scan': "",
    })

    phantom.act("scan network", parameters=parameters, assets=['nmap'], callback=format_1, name="scan_network_1", parent_action=action)

    return

def execute_program_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('execute_program_1() called')

    # collect data for 'execute_program_1' call

    parameters = []
    
    # build parameters list for 'execute_program_1' call
    parameters.append({
        'command': "sudo -b openvpn /home/user/sorsnce.ovpn",
        'timeout': "",
        'ip_hostname': "phantom.sorsnce.com",
        'script_file': "",
    })

    phantom.act("execute program", parameters=parameters, assets=['phantom-ssh'], callback=scan_network_1, name="execute_program_1")

    return

def execute_program_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('execute_program_2() called')
    
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'execute_program_2' call

    parameters = []
    
    # build parameters list for 'execute_program_2' call
    parameters.append({
        'ip_hostname': "phantom.sorsnce.com",
        'command': "sudo kill $(ps aux | grep openvpn | awk '{print $2}')",
        'script_file': "",
        'timeout': "",
    })

    phantom.act("execute program", parameters=parameters, assets=['phantom-ssh'], name="execute_program_2", parent_action=action)

    return

def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('format_1() called')
    
    template = """Investigate the following Ports:

{0}"""

    # parameter list for template variable replacement
    parameters = [
        "scan_network_1:action_result.data.*.tcp.*.name",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_1")

    send_message_2(container=container)

    return

def send_message_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('send_message_2() called')
    
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'send_message_2' call
    formatted_data_1 = phantom.get_format_data(name='format_1')

    parameters = []
    
    # build parameters list for 'send_message_2' call
    parameters.append({
        'destination': "#personal-monitor",
        'message': formatted_data_1,
    })

    phantom.act("send message", parameters=parameters, assets=['slack'], callback=execute_program_2, name="send_message_2")

    return

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    # This function is called after all actions are completed.
    # summary of all the action and/or all detals of actions 
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    return