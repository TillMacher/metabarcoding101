# Glossary

Amplicon
: The DNA fragment amplified by PCR with a specific primer pair.

BIN
: Barcode Index Number – a cluster of COI sequences on BOLD that roughly corresponds to a species.

Chimera
: An artificial sequence formed from two different templates during PCR. Removed during processing.

Demultiplexing
: Sorting pooled reads back into their original samples using tags/barcodes.

Denoising
: Removing sequencing errors to obtain exact sequence variants (ESVs).

Dereplication
: Collapsing identical sequences into one, keeping track of how often each occurred.

ESV
: Exact sequence variant – a unique, denoised sequence.

E-value
: The number of hits of similar quality expected by chance in a BLAST search. Lower is better.

Inline tag
: A short sequence added in front of the primer to label which sample a read belongs to.

Negative control (NC)
: A sample without template DNA, used to detect contamination.

OTU
: Operational taxonomic unit – a cluster of similar sequences (e.g. 97 % similarity).

Paired-end merging
: Combining the forward (R1) and reverse (R2) read of a fragment into one sequence.

Primer trimming
: Removing the primer sequences from the reads.

Quality filtering
: Removing reads with too many expected errors or an unexpected length.

Read table
: ESVs/OTUs × samples with read counts (output of APSCALE).

Reference database
: A collection of sequences with known taxonomy used for taxonomic assignment (e.g. BOLD, MIDORI2, SILVA).

Replicate
: A repeated PCR or sample from the same source, used to check reliability.

Swarm clustering
: An OTU clustering method that groups sequences iteratively by small differences, without a fixed threshold.

Taxon table
: A table of ESVs/OTUs × samples with read counts and taxonomic assignments (the main input for TTT).

Taxonomy table
: The taxonomic assignment of each ESV/OTU (output of APSCALE-blast or BOLDigger3).

```{todo}
Add more terms.
```
