#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu

import mpu6050
import glm


class MPU6050Node(Node):

    def __init__(self):
        super().__init__("mpu6050_publisher")
        try:
            self.mpu6050 = mpu6050.mpu6050(0x68)
        except Exception:
            self.mpu6050 = mpu6050.mpu6050(0x69)

        self.initial_accel = glm.vec3(**self.mpu6050.get_accel_data())
        self.initial_gyro = glm.vec3(**self.mpu6050.get_gyro_data())

        self.mpu6050_publisher = self.create_publisher(Imu, "/mpu6050", 10)

        self.past = self.get_clock().now().seconds_nanoseconds()
        self.past = self.sec_nano_to_float(self.past)
        self.create_timer(1/60, self.timer_callback)

    def timer_callback(self):
        imu = Imu()
        accel = glm.vec3(**self.mpu6050.get_accel_data())
        gyro = glm.vec3(**self.mpu6050.get_gyro_data()) - self.initial_gyro
        gyro = glm.radians(gyro)
        temp = self.mpu6050.get_temp()

        time = self.get_clock().now()
        now = time.seconds_nanoseconds()
        now = self.sec_nano_to_float(now)
        delta_time = now - self.past # TODO: usar esta wea para determinar la orientacion aproximada en base a la velocidad angular (a mayor frecuencia mayor la precisión)
        # print(delta_time)
        imu.header.stamp = time.to_msg()
        imu.angular_velocity.x, imu.angular_velocity.y, imu.angular_velocity.z = gyro.to_list()
        imu.linear_acceleration.x, imu.linear_acceleration.y, imu.linear_acceleration.z = accel.to_list()

        self.mpu6050_publisher.publish(imu)
        self.past = now
        # self.get_logger().info(f"data:\n{accel}\n{gyro}\n{temp}")
        # self.get_logger().info(str(imu))
    
    def sec_nano_to_float(self, t: tuple[int, int]):
        """Combina la tupla (segundos, nanosegundos) en
        una sola variable float transformardo los nanosegundos
        en segundos."""
        return t[0] + t[1] * 1e-9


def main(args=None):
    rclpy.init(args=args)
    node = MPU6050Node()
    rclpy.spin(node)
    rclpy.shutdown()
