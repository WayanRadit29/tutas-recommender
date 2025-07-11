from generators import generate_murid, generate_tutor, generate_interaksi

def main():
    # 1) Generate data
    df_murid     = generate_murid()
    df_tutor     = generate_tutor()
    df_interaksi = generate_interaksi(df_murid, df_tutor)
    
    # 2) Simpan ke file CSV
    df_murid.to_csv('murid.csv', index=False)
    df_tutor.to_csv('tutor.csv', index=False)
    df_interaksi.to_csv('interaksi.csv', index=False)
    
    print("✅ Berhasil generate:")
    print("   • murid.csv      ({} baris)".format(len(df_murid)))
    print("   • tutor.csv      ({} baris)".format(len(df_tutor)))
    print("   • interaksi.csv  ({} baris)".format(len(df_interaksi)))

if __name__ == '__main__':
    main()
