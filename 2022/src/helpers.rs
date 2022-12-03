/*
 * Use this file if you want to extract helpers from your solutions.
 * Example import from this file: `use advent_of_code::helpers::example_fn;`.
 */

use std::collections::HashSet;

pub fn parse_input<T>(input: &str, cons: fn(&str) -> T) -> Vec<T>
where
    Vec<T>: FromIterator<T>,
{
    input.lines().map(cons).collect()
}
