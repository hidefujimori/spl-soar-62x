"""
this is loop test
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'prompt_1' block
    prompt_1(container=container)

    return

@phantom.playbook_block()
def prompt_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("prompt_1() called")

    # set user and message variables for phantom.prompt call

    user = ""
    role = None
    message = """"""

    # parameter list for template variable replacement
    parameters = []

    phantom.prompt2(container=container, user=user, role=role, message=message, respond_in_mins=30, name="prompt_1", parameters=parameters, callback=get_cached_entries_1)

    return


@phantom.playbook_block()
def loop_get_cached_entries_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("loop_get_cached_entries_1() called")

    loop_state = phantom.LoopState(state=loop_state_json)

    if loop_state.should_continue(container=container, results=results): # should_continue evaluates iteration/timeout/conditions
        loop_state.increment() # increments iteration count
        get_cached_entries_1(container=container, loop_state_json=loop_state.to_json())
    else:
        add_note_1(container=container)

    return


@phantom.playbook_block()
def get_cached_entries_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("get_cached_entries_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    parameters = []

    if not loop_state_json:
        # Loop state is empty. We are creating a new one from the inputs
        loop_state_json = {
            # Looping configs
            "current_iteration": 1,
            "max_iterations": 2,
            "conditions": None,
            "max_ttl": 600,
            "delay_time": 120,
        }

    # Load state from the JSON passed to it
    loop_state = phantom.LoopState(state=loop_state_json)

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("get cached entries", parameters=parameters, name="get_cached_entries_1", assets=["virustotal-v3"], callback=loop_get_cached_entries_1, loop_state=loop_state.to_json())

    return


@phantom.playbook_block()
def add_note_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_note_1() called")

    get_cached_entries_1_result_data = phantom.collect2(container=container, datapath=["get_cached_entries_1:action_result.data"], action_results=results)

    get_cached_entries_1_result_item_0 = [item[0] for item in get_cached_entries_1_result_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.add_note(container=container, content=get_cached_entries_1_result_item_0, note_format="markdown", note_type="general", title="test")

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    return