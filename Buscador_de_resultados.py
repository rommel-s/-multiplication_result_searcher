{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Buscador de resultados",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rommel-s/-multiplication_result_searcher/blob/master/Buscador_de_resultados.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fLE3DGiwPnGU",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "val = int(input('Digite o valor a ser pesquisado: '))\n",
        "for a in range(0, 2000):\n",
        "  for h in range(0, 2000):\n",
        "    valor = a * h\n",
        "    if valor == val:\n",
        "      print(f'{a} x {h} = {valor}')\n",
        "      \n",
        "      "
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}