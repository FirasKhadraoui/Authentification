package com.sfm.microservice.repository;

import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.sfm.microservice.entities.User;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByUsername(String username);
    Optional<User> findById(int username);
    List<User> findByActive(boolean etat);
    Boolean existsByUsername(String id);
    List<User> findByRole(int role);
}
