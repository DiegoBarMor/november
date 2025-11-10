#!/bin/bash
set -eu

printf "TEST 01: PROT... "

start_time=$(date +%s)
output="$(python3 main.py prot tests/data/prot.pdb)"
end_time=$(date +%s)

expected="$(cat <<'EOF'
>>> Amber energies (November) for 'tests/data/prot.pdb':
  BondEnergy: 535.5952440258552
  AngleEnergy: 1740.148996314636
  DihedEnergy: 1632.2866727153953
  Nonbonded: -3755.386936876314
  ... LennardJones: -415.9121389249436
  ... Coulomb: -3339.4747979513704
EOF
)"

if [ "$output" != "$expected" ]; then
  printf "Output did not match expected.\n\n=== Output ===\n%s\n\n=== Expected ===\n%s\n" "$output" "$expected"
  exit 1
fi

printf "OK (%d seconds)\n" $((end_time - start_time))
