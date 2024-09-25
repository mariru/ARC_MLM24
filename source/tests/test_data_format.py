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

# Run the tests using the loaded data
def test_submission_format_with_json_data():
    with open('../../data/sample_submission.json', 'r') as f:
        submission = json.load(f)
    with open('../../data/arc-agi_test_challenges.json', 'r') as f:
        test_challenges = json.load(f)
    validate_submission_format(submission, test_challenges)