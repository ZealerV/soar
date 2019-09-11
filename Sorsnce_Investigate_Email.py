"""
This playbook will take the following data and run through recon modules:

new stuff

Actions include:

Phantom DNS
Phantom IP
VirusTotal
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

##############################
# Start - Global Code Block

import sys
import urllib 
import urlparse
import time

# End - Global Code block
##############################

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'filter_14' block
    filter_14(container=container)

    # call 'filter_16' block
    filter_16(container=container)

    # call 'filter_12' block
    filter_12(container=container)

    # call 'filter_20' block
    filter_20(container=container)

    return

def filter_12(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('filter_12() called')

    # collect filtered artifact ids for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["artifact:*.cef.requestURL", ">=", "1"],
        ],
        name="filter_12:condition_1")

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        playbook_soar_Sorsnce_URL_Recon_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return

def filter_14(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('filter_14() called')

    # collect filtered artifact ids for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["artifact:*.cef.destinationAddress", ">=", "1"],
        ],
        name="filter_14:condition_1")

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        playbook_soar_Sorsnce_IP_Recon_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return

def filter_16(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('filter_16() called')

    # collect filtered artifact ids for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["artifact:*.cef.destinationDnsDomain", ">=", "1"],
        ],
        name="filter_16:condition_1")

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        playbook_soar_Sorsnce_Domain_Recon_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return

def filter_20(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('filter_20() called')

    # collect filtered artifact ids for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["artifact:*.cef.fileHashSha256", ">=", "1"],
            ["artifact:*.cef.fileHashMd5", ">=", "1"],
            ["artifact:*.cef.fileHashSha1", ">=", "1"],
            ["artifact:*.cef.fileHashSha512", ">=", "1"],
        ],
        logical_operator='or',
        name="filter_20:condition_1")

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        playbook_soar_Sorsnce_Hash_Recon_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return

def playbook_soar_Sorsnce_URL_Recon_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('playbook_soar_Sorsnce_URL_Recon_1() called')
    
    # call playbook "soar/Sorsnce_URL_Recon", returns the playbook_run_id
    playbook_run_id = phantom.playbook("soar/Sorsnce_URL_Recon", container=container, name="playbook_soar_Sorsnce_URL_Recon_1")

    return

def playbook_soar_Sorsnce_Hash_Recon_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('playbook_soar_Sorsnce_Hash_Recon_1() called')
    
    # call playbook "soar/Sorsnce_Hash_Recon", returns the playbook_run_id
    playbook_run_id = phantom.playbook("soar/Sorsnce_Hash_Recon", container=container, name="playbook_soar_Sorsnce_Hash_Recon_1")

    return

def playbook_soar_Sorsnce_IP_Recon_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('playbook_soar_Sorsnce_IP_Recon_1() called')
    
    # call playbook "soar/Sorsnce_IP_Recon", returns the playbook_run_id
    playbook_run_id = phantom.playbook("soar/Sorsnce_IP_Recon", container=container)

    return

def playbook_soar_Sorsnce_Domain_Recon_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('playbook_soar_Sorsnce_Domain_Recon_1() called')
    
    # call playbook "soar/Sorsnce_Domain_Recon", returns the playbook_run_id
    playbook_run_id = phantom.playbook("soar/Sorsnce_Domain_Recon", container=container, name="playbook_soar_Sorsnce_Domain_Recon_1")

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