import pytest
import json

def validate_grid(grid):
    """
    Make sure that the grid is a list of lists of integers between 0 and 9. 
    The length of each list is at most 30. The length of all the sublists is the same (also capped at 30).
    """
    grid_len = len(grid)
    if grid_len == 0:
        return
    row_len = len(grid[0])

    assert isinstance(grid, list)
    assert all(isinstance(row, list) for row in grid)

    assert all(all(isinstance(i, int) for i in row) for row in grid)
    assert all(all(0 <= i <= 9 for i in row) for row in grid)
    
    assert grid_len <= 30
    assert row_len <= 30
    assert all(len(row) == row_len for row in grid)


def validate_point_cloud(point_cloud):
    # need to finish
    pass

def validate_submission_format(submission, test_challenges):
    """
    Make sure that submission is a dictionary with the same keys as test_challenges. 
    For each key called task_id, submission[task_id] is a list of the same length as test_challenges[task_id].
    Each element of this list is a dictionary with two keys, "attempt_1" and "attempt_2".
    Each value is a grid that satisfies the constraints of test_grid.
    """
    assert isinstance(submission, dict)
    assert set(submission.keys()) == set(test_challenges.keys())
    
    for task_id, task_variations in submission.items():
        assert isinstance(task_variations, list)
        assert len(task_variations) == len(test_challenges[task_id]['test'])
        for task_instance in task_variations:
            assert isinstance(task_instance, dict)
            assert set(task_instance.keys()) == {"attempt_1", "attempt_2"}
            validate_grid(task_instance["attempt_1"])
            validate_grid(task_instance["attempt_2"])

def validate_training_challenge_format(challenges):
    """
    Make sure training_challenges[task_id] is a dict with keys train and test. 
    Make sure training_challenges[task_id][train] contains a list of pairs. Each pair is a dict with keys input and output
    """
    for task_id, task in challenges.items():
        assert set(task.keys()) == {"train", "test"}
        assert isinstance(task["train"], list)
        assert all(isinstance(pair, dict) for pair in task["train"])
        assert all(set(pair.keys()) == {"input", "output"} for pair in task["train"])
        assert isinstance(task["test"], list)
        assert all(isinstance(d, dict) for d in task["test"])
        assert all(set(d.keys()) == {"input"} for d in task["test"])
        for pair in task["train"]:
            validate_grid(pair["input"])
            validate_grid(pair["output"])
        for d in task["test"]:
            validate_grid(d["input"])

def validate_training_solution_format(solutions):
    """
    Make sure training_solutions[task_id][test] list of dicts with single key "input". 
    For all i, training_solutions[task_id][test][i][input] is a grid.
    """
    for task_id, task in solutions.items():
        assert isinstance(task, list)
        for grid in task:
            validate_grid(grid)

def validate_challenge_w_solutions_format(challenges, solutions):
    """
    Make sure that training_challenges and training_solutions contains the same task ids
    Then check respective formats.
    """

    assert isinstance(challenges, dict)
    assert isinstance(solutions, dict)
    assert set(challenges.keys()) == set(solutions.keys())
    validate_training_challenge_format(challenges)
    validate_training_solution_format(solutions)
    for task_id, task in challenges.items():
        assert len(task["test"]) == len(solutions[task_id])

def test_puzzle_generator():
    """
    Puzzle_Generator = Color_Map()
    training_challenges, training_solutions = Puzzle_Generator.sample(10)
    #map outputs to dictionary
    validate_challenge_w_solutions_format(training_challenges, training_solutions)
    """
    pass

# Run the tests using the loaded data
def test_submission_format_with_json_data():
    with open('../../data/sample_submission.json', 'r') as f:
        submission = json.load(f)
    with open('../../data/arc-agi_test_challenges.json', 'r') as f:
        test_challenges = json.load(f)
    validate_submission_format(submission, test_challenges)

def test_training_inputs_with_json_data():
    with open('../../data/arc-agi_training_challenges.json', 'r') as f:
        training_challenges = json.load(f)
    with open('../../data/arc-agi_training_solutions.json', 'r') as f:
        training_solutions = json.load(f)
    validate_challenge_w_solutions_format(training_challenges, training_solutions)

    with open('../../data/arc-agi_evaluation_challenges.json', 'r') as f:
        training_challenges = json.load(f)
    with open('../../data/arc-agi_evaluation_solutions.json', 'r') as f:
        training_solutions = json.load(f)
    validate_challenge_w_solutions_format(training_challenges, training_solutions)