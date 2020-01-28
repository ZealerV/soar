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

    # collect data for 'scan_network_1' call
    container_data = phantom.collect2(container=container, datapath=['artifact:*.cef.deviceAddress', 'artifact:*.id'])

    parameters = []
    
    # build parameters list for 'scan_network_1' call
    for container_item in container_data:
        if container_item[0]:
            parameters.append({
                'ip_hostname': container_item[0],
                'portlist': "",
                'udp_scan': "",
                'script': "",
                'script-args': "-A",
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': container_item[1]},
            })

    phantom.act("scan network", parameters=parameters, assets=['nmap'], name="scan_network_1")

    return

def execute_program_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('execute_program_1() called')

    # collect data for 'execute_program_1' call

    parameters = []
    
    # build parameters list for 'execute_program_1' call
    parameters.append({
        'ip_hostname': "phantom.sorsnce.com",
        'command': "openvpn /home/user/sorsnce.ovpn",
        'script_file': "",
        'timeout': "",
    })

    phantom.act("execute program", parameters=parameters, assets=['phantom-ssh'], name="execute_program_1")

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