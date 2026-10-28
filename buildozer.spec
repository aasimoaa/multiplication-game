name: Build Android APK

on:
  workflow_dispatch:
  push:
    branches: [ "main", "master" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install System Dependencies
      run: |
        sudo apt update
        sudo apt install -y git zip unzip openjdk-17-jdk autoconf libtool pkg-config zlib1g-dev libncurses-dev libtinfo6 cmake libffi-dev libssl-dev

    - name: Install Buildozer and Cython
      run: |
        pip install --upgrade pip
        pip install Cython==0.29.37 buildozer

    - name: Build with Buildozer
      run: |
        buildozer -v android debug

    - name: Upload APK Artifact
      uses: actions/upload-artifact@v4
      with:
        name: Multiplication-Hero-APK
        path: bin/*.apk
