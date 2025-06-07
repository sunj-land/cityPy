import tensorflow as tf
import time

# 创建一个大矩阵进行计算测试


def test_gpu_performance():
    # 创建大矩阵
    matrix_size = 2000
    a = tf.random.normal([matrix_size, matrix_size])
    b = tf.random.normal([matrix_size, matrix_size])

    start_time = time.time()

    c = tf.matmul(a, b)

    # 修改这行，将结果转换为浮点数
    tf.debugging.assert_greater(tf.cast(tf.reduce_sum(c), tf.float32), 0.0)

    duration = time.time() - start_time
    print(f"矩阵大小: {matrix_size}x{matrix_size}")
    print(f"计算耗时: {duration:.2f} 秒")

    flops = 2 * matrix_size * matrix_size * matrix_size
    gflops = flops / (duration * 1e9)
    print(f"理论性能: {gflops:.2f} GFLOPS")


# 运行测试
print("GPU 设备信息:")
print(tf.config.list_physical_devices('GPU'))
print("\n开始性能测试...")
test_gpu_performance()
