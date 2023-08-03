## $\mathbf{P}$-可積分でない確率変数の例（cf. サンクトペテルブルクのパラドックス）

- 標本空間 $\Omega := \{ 1,2,3,\ldots \}$
- 確率 $\mathbf{P}(\{\omega\}) := 1/2^{\omega}$
  - 全確率の和はちゃんと $1/2+1/4+1/8+\cdots=1$ になっている
- 確率変数 $X(\omega) := 2^{\omega}$
- このとき， $\sum_{\omega\in\Omega}|X(\omega)|\mathbf{P}(\{\omega\})=\sum_{\omega\in\Omega}2^{\omega}\cdot(1/2^{\omega})=1+1+\cdots=\infty$
- よって，この $X$ は $\mathbf{P}$-可積分でない確率変数である．

## $X$ は $\mathbf{P}$-可積分だが $X^2$ は $\mathbf{P}$-可積分でない確率変数の例
上記のちょっとした応用．

- 標本空間 $\Omega := \{ 1,2,3,\ldots \}$
- 確率 $\mathbf{P}(\{\omega\}) := 1/2^{\omega}$
- 確率変数 $X(\omega) := 2^{\omega/2}$
- このとき，
  - $\sum_{\omega\in\Omega}|X(\omega)|\mathbf{P}(\{\omega\})=\sum_{\omega\in\Omega}2^{\omega/2}\cdot(1/2^{\omega})=\sum_{\omega=1}^{\infty}(1/\sqrt{2})^\omega=1+\sqrt{2}$
    - よって，$X$ は $\mathbf{P}$-可積分である．
  - $\sum_{\omega\in\Omega}|(X(\omega))^2|\mathbf{P}(\{\omega\})=\sum_{\omega\in\Omega}2^{\omega}\cdot(1/2^{\omega})=1+1+\cdots=\infty$
    - よって，$X^2$ は $\mathbf{P}$-可積分でない．
