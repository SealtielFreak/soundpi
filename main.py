import soundpi


if __name__ == "__main__":
    try:
        soundpi.app.run(debug=True)
    except KeyboardInterrupt:
        soundpi.app.shutdown()
