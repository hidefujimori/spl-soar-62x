"""
test
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'add_note_1' block
    add_note_1(container=container)
    # call 'get_playbook_tree_1' block
    get_playbook_tree_1(container=container)

    return

@phantom.playbook_block()
def add_note_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_note_1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.add_note(container=container, content="タイマーアプリによって実行", note_format="markdown", note_type="general", title="Timer app worked")

    container = phantom.get_container(container.get('id', None))

    return


@phantom.playbook_block()
def get_playbook_tree_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("get_playbook_tree_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    launching_user_data = phantom.collect2(container=container, datapath=["playbook:launching_user.id"])

    parameters = []

    # build parameters list for 'get_playbook_tree_1' call
    for launching_user_item in launching_user_data:
        parameters.append({
            "playbook_run_id": launching_user_item[0],
            "include_app_runs": True,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("get playbook tree", parameters=parameters, name="get_playbook_tree_1", assets=["pbtree"], callback=add_note_3)

    return


@phantom.playbook_block()
def add_note_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_note_3() called")

    get_playbook_tree_1_result_data = phantom.collect2(container=container, datapath=["get_playbook_tree_1:action_result.data"], action_results=results)

    get_playbook_tree_1_result_item_0 = [item[0] for item in get_playbook_tree_1_result_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.add_note(container=container, content=get_playbook_tree_1_result_item_0, note_format="markdown", note_type="general", title="Playbook")

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