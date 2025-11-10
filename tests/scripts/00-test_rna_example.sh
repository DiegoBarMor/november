#!/bin/bash
set -eu

printf "TEST 00: RNA... "

start_time=$(date +%s)
output="$(python3 main.py rna tests/data/1ato.pdb)"
end_time=$(date +%s)

expected="$(cat <<'EOF'
>>> Amber energies (November) for 'tests/data/1ato.pdb':
  BondEnergy: 136.737504951933
  AngleEnergy: 172.93445492701437
  DihedEnergy: 1976.3687249939167
  Nonbonded: 3783.160178132041
  ... LennardJones: 4084.5852277482977
  ... Coulomb: -301.42504961625673
EOF
)"

if [ "$output" != "$expected" ]; then
  printf "Output did not match expected.\n\n=== Output ===\n%s\n\n=== Expected ===\n%s\n" "$output" "$expected"
  exit 1
fi

printf "OK (%d seconds)\n" $((end_time - start_time))
