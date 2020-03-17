test = {
  'name': 'q3_10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.random.seed(123);
          >>> np.isclose(round(simulate_and_test_statistic(change_in_death_rates, "Death Penalty", "Murder Rate"), 3) - (-1.398), 0)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
