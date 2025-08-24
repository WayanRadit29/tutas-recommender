from pathlib import Path
from generators import generate_murid, generate_tutor, generate_interaksi


def main():
    """
    Main entry point for synthetic dataset generation.

    Steps:
        1. Generate three datasets:
            - Students (murid)
            - Tutors (tutor)
            - Interactions (interaksi)
        2. Save them as CSV files inside dataset/unprocessed/.
        3. Print a summary of generated file sizes.
    """

    # 1. Generate datasets
    df_murid     = generate_murid()
    df_tutor     = generate_tutor(df_murid)
    df_interaksi = generate_interaksi(df_murid, df_tutor)

    # 2. Ensure target directory exists
    output_dir = Path("dataset/unprocessed")
    output_dir.mkdir(parents=True, exist_ok=True)

    # 3. Save CSV files
    df_murid.to_csv(output_dir / "murid.csv", index=False)
    df_tutor.to_csv(output_dir / "tutor.csv", index=False)
    df_interaksi.to_csv(output_dir / "interaksi.csv", index=False)

    # 4. Print summary
    print("✅ Synthetic datasets generated successfully:")
    print("   • murid.csv      ({} rows)".format(len(df_murid)))
    print("   • tutor.csv      ({} rows)".format(len(df_tutor)))
    print("   • interaksi.csv  ({} rows)".format(len(df_interaksi)))


if __name__ == "__main__":
    main()
